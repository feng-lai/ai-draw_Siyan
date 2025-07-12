import express from "express"
import cors from "cors"
import { spawn } from "child_process"
import path from "path"
import fs from "fs"
import { fileURLToPath } from "url"

const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

const app = express()
const PORT = 3001

app.use(cors())
app.use(express.json())
app.use("/images", express.static(path.join(__dirname, "generated_images")))

// Ensure the generated_images directory exists
const imagesDir = path.join(__dirname, "generated_images")
if (!fs.existsSync(imagesDir)) {
  fs.mkdirSync(imagesDir, { recursive: true })
}

app.post("/api/generate-image", async (req, res) => {
  const { prompt } = req.body

  if (!prompt) {
    return res.status(400).json({ error: "Prompt is required" })
  }

  try {
    console.log("Generating image for prompt:", prompt)

    // Create a unique filename for this generation
    const timestamp = Date.now()
    const filename = `generated_${timestamp}.png`
    const outputPath = path.join(imagesDir, filename)

    // Spawn Python process
    const pythonProcess = spawn("python", [path.join(__dirname, "scripts", "image_generator.py"), prompt, outputPath])

    let stdout = ""
    let stderr = ""

    pythonProcess.stdout.on("data", (data) => {
      stdout += data.toString()
      console.log("Python stdout:", data.toString())
    })

    pythonProcess.stderr.on("data", (data) => {
      stderr += data.toString()
      console.error("Python stderr:", data.toString())
    })

    pythonProcess.on("close", (code) => {
      if (code === 0) {
        // Check if the image file was created
        if (fs.existsSync(outputPath)) {
          res.json({
            success: true,
            imageUrl: `/images/${filename}`,
            message: "Image generated successfully",
          })
        } else {
          res.status(500).json({
            error: "Image generation completed but file not found",
            details: stdout,
          })
        }
      } else {
        res.status(500).json({
          error: "Image generation failed",
          details: stderr || stdout,
          code,
        })
      }
    })

    pythonProcess.on("error", (error) => {
      console.error("Failed to start Python process:", error)
      res.status(500).json({
        error: "Failed to start image generation process",
        details: error.message,
      })
    })
  } catch (error) {
    console.error("Server error:", error)
    res.status(500).json({
      error: "Internal server error",
      details: error.message,
    })
  }
})

// Health check endpoint
app.get("/api/health", (req, res) => {
  res.json({ status: "OK", message: "Image generation API is running" })
})

app.listen(PORT, () => {
  console.log(`Image generation API server running on http://localhost:${PORT}`)
  console.log(`Generated images will be served from http://localhost:${PORT}/images/`)
})
