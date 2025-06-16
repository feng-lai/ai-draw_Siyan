<template>
  <div class="editor-layout">
    <div class="top-nav">
      <div class="left-controls">
        <button class="home-button">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
            <polyline points="9 22 9 12 15 12 15 22" />
          </svg>
        </button>
        <div class="document-info">
          <span class="doc-title">AI Image Generator</span>
          <span class="doc-size">1536 × 1536</span>
        </div>
      </div>

      <div class="center-controls">
        <button class="tool-button play-button" @click="generateImage" :disabled="isGenerating">
          <svg v-if="!isGenerating" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"
            fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="5 3 19 12 5 21 5 3" />
          </svg>
          <svg v-else xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="animate-spin">
            <path d="M21 12a9 9 0 11-6.219-8.56" />
          </svg>
        </button>
      </div>

      <div class="right-controls">
        <div class="credits">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none"
            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10" />
            <path d="M16 8h-6.5a2.5 2.5 0 0 0 0 5h3a2.5 2.5 0 0 1 0 5H6" />
            <path d="M12 18v2m0-16v2" />
          </svg>
          <span>{{ credits }}</span>
        </div>
        <button class="export-button" @click="exportImage" :disabled="!generatedImage">Export</button>
      </div>
    </div>

    <div class="editor-container">
      <div class="icon-sidebar" :class="{ 'expanded': sidebarExpanded }">
        <button class="sidebar-toggle" @click="toggleSidebar">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path v-if="sidebarExpanded" d="M18 15 12 9l-6 6" />
            <path v-else d="M6 9l6 6 6-6" />
          </svg>
        </button>

        <button class="icon-button" :class="{ active: activeTool === 'Text to Image' }"
          @click="setActiveTool('Text to Image')">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 7V4h16v3" />
            <path d="M9 20h6" />
            <path d="M12 4v16" />
          </svg>
          <span>Txt2Img</span>
        </button>

        <button class="icon-button" :class="{ active: activeTool === 'Edit Image' }"
          @click="setActiveTool('Edit Image')">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 20h9" />
            <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z" />
          </svg>
          <span>EditImg</span>
        </button>
      </div>

      <div class="tool-panel" v-if="activeTool">
        <div class="tool-panel-header">
          <h3>{{ activeTool }}</h3>
          <button class="close-panel-btn" @click="closeTool">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
              stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M18 6 6 18" />
              <path d="m6 6 12 12" />
            </svg>
          </button>
        </div>

        <div class="tool-panel-content" v-if="activeTool === 'Text to Image'">
          <div class="model-selector">
            <div class="model-preview">
              <div class="model-icon">🤖</div>
              <span>Gemini 2.0 Flash</span>
            </div>
          </div>

          <div class="prompt-area">
            <textarea class="prompt-input" placeholder="描述你想创建的内容（支持20种语言）" v-model="textToImagePrompt"
              @keydown.ctrl.enter="generateImage"></textarea>
            <div class="prompt-counter">{{ textToImagePrompt.length }} / 1800</div>

            <div class="option-row">
              <div class="option-label">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect width="18" height="18" x="3" y="3" rx="2" ry="2" />
                </svg>
                <span>Aspect Ratio</span>
              </div>
              <div class="aspect-value">1024×1536</div>
            </div>

            <div class="aspect-buttons">
              <button class="aspect-button">3:4</button>
              <button class="aspect-button active">1:1</button>
              <button class="aspect-button">4:3</button>
            </div>

            <div class="generation-status" v-if="isGenerating">
              <div class="status-indicator">
                <div class="spinner"></div>
                <span>正在生成图片...</span>
              </div>
              <div class="progress-bar">
                <div class="progress-fill" :style="{ width: progress + '%' }"></div>
              </div>
            </div>

            <div class="error-message" v-if="errorMessage">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none"
                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10" />
                <line x1="15" y1="9" x2="9" y2="15" />
                <line x1="9" y1="9" x2="15" y2="15" />
              </svg>
              <span>{{ errorMessage }}</span>
            </div>
          </div>

          <button class="generate-button" @click="generateImage" :disabled="isGenerating || !textToImagePrompt.trim()">
            <span v-if="!isGenerating">Generate</span>
            <span v-else>Generating...</span>
            <span class="generate-label">AI</span>
            <span class="credit-amount">4</span>
          </button>
        </div>

        <div class="tool-panel-content" v-else-if="activeTool === 'Edit Image'">
          <div class="model-selector">
            <div class="model-preview">
              <div class="model-icon">🤖</div>
              <span>Gemini 2.0 Flash</span>
            </div>
          </div>

          <div class="upload-area">
            <input type="file" ref="imageUpload" @change="handleImageUpload" accept="image/*" style="display: none;">
            <button class="upload-button" @click="triggerImageUpload">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 0 9H3a2 2 0 0 1 0-4h1v1Z"/>
                <path d="M12 12v9"/>
                <path d="m16 16-4-4-4 4"/>
              </svg>
              {{ uploadedImageName || 'Upload Image' }}
            </button>
            <div v-if="uploadedImagePreview" class="image-upload-preview">
              <img :src="uploadedImagePreview" alt="Uploaded Image" />
            </div>
          </div>

          <div class="prompt-area">
            <textarea class="prompt-input" placeholder="描述你想如何编辑图片（支持20种语言）" v-model="editImagePrompt"
              @keydown.ctrl.enter="editImage"></textarea>
            <div class="prompt-counter">{{ editImagePrompt.length }} / 1800</div>

            <div class="generation-status" v-if="isGenerating">
              <div class="status-indicator">
                <div class="spinner"></div>
                <span>正在编辑图片...</span>
              </div>
              <div class="progress-bar">
                <div class="progress-fill" :style="{ width: progress + '%' }"></div>
              </div>
            </div>

            <div class="error-message" v-if="errorMessage">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none"
                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10" />
                <line x1="15" y1="9" x2="9" y2="15" />
                <line x1="9" y1="9" x2="15" y2="15" />
              </svg>
              <span>{{ errorMessage }}</span>
            </div>
          </div>

          <button class="generate-button" @click="editImage" :disabled="isGenerating || !editImagePrompt.trim() || !uploadedImageFile">
            <span v-if="!isGenerating">Edit Image</span>
            <span v-else>Editing...</span>
            <span class="generate-label">AI</span>
            <span class="credit-amount">4</span>
          </button>
        </div>
      </div>

      <div class="canvas-area">
        <div class="canvas-content">
          <div v-if="!generatedImage && !isGenerating" class="canvas-placeholder">
            <div class="placeholder-content">
              <div class="placeholder-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect width="18" height="18" x="3" y="3" rx="2" />
                  <circle cx="9" cy="9" r="2" />
                  <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21" />
                </svg>
              </div>
              <h2>AI Image Generator</h2>
              <p>使用左侧的"Text to Image"工具开始创建图片</p>
            </div>
          </div>

          <div v-if="isGenerating" class="generation-preview">
            <div class="generation-placeholder">
              <div class="generation-spinner">
                <div class="spinner-ring"></div>
              </div>
              <h3>正在生成您的图片...</h3>
              <p>{{ activeTool === 'Text to Image' ? textToImagePrompt : editImagePrompt }}</p>
            </div>
          </div>

          <div v-if="generatedImage" class="image-result">
            <img :src="generatedImage" alt="Generated Image" class="generated-image" />
            <div class="image-actions">
              <button class="action-btn" @click="downloadImage">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
                  <polyline points="7 10 12 15 17 10" />
                  <line x1="12" y1="15" x2="12" y2="3" />
                </svg>
                下载
              </button>
              <button class="action-btn" @click="regenerateImage">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M1 4v6h6" />
                  <path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10" />
                </svg>
                重新生成
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

// State management
const activeTool = ref('Text to Image');
const sidebarExpanded = ref(false);
const textToImagePrompt = ref('A red apple on a wooden table, photorealistic');
const editImagePrompt = ref(''); // New state for edit image prompt
const uploadedImageFile = ref(null); // New state for uploaded image file
const uploadedImagePreview = ref(null); // New state for image preview
const uploadedImageName = ref(''); // New state for uploaded image name
const isGenerating = ref(false);
const generatedImage = ref(null);
const errorMessage = ref('');
const progress = ref(0);
const credits = ref(50);

// API configuration
const API_BASE_URL = '';

// Refs for direct DOM access
const imageUpload = ref(null);

// Toggle sidebar
const toggleSidebar = () => {
  sidebarExpanded.value = !sidebarExpanded.value;
};

// Set active tool
const setActiveTool = (tool) => {
  activeTool.value = tool;
  // Clear generated image and prompt when switching tools
  generatedImage.value = null;
  errorMessage.value = '';
  if (tool === 'Text to Image') {
    editImagePrompt.value = '';
    uploadedImageFile.value = null;
    uploadedImagePreview.value = null;
    uploadedImageName.value = '';
  } else if (tool === 'Edit Image') {
    textToImagePrompt.value = '';
  }
};

// Close tool panel
const closeTool = () => {
  activeTool.value = null;
  generatedImage.value = null;
  errorMessage.value = '';
};

// Handle image upload for Edit Image tool
const triggerImageUpload = () => {
  imageUpload.value.click();
};

const handleImageUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    uploadedImageFile.value = file;
    uploadedImageName.value = file.name;
    const reader = new FileReader();
    reader.onload = (e) => {
      uploadedImagePreview.value = e.target.result;
    };
    reader.readAsDataURL(file);
  } else {
    uploadedImageFile.value = null;
    uploadedImagePreview.value = null;
    uploadedImageName.value = '';
  }
};

// Generate image function (for Text to Image)
const generateImage = async () => {
  if (!textToImagePrompt.value.trim() || isGenerating.value) {
    return;
  }

  isGenerating.value = true;
  errorMessage.value = '';
  progress.value = 0;
  generatedImage.value = null;

  const progressInterval = setInterval(() => {
    if (progress.value < 90) {
      progress.value += Math.random() * 10;
    }
  }, 500);

  try {
    const response = await fetch(`/api/generate-image`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        prompt: textToImagePrompt.value
      })
    });

    const data = await response.json();

    if (response.ok && data.success) {
      generatedImage.value = `${API_BASE_URL}${data.imageUrl}`;
      credits.value = Math.max(0, credits.value - 4);
      progress.value = 100;
    } else {
      throw new Error(data.error || 'Generation failed');
    }
  } catch (error) {
    console.error('Error generating image:', error);
    errorMessage.value = error.message || '生成图片时发生错误，请重试';
  } finally {
    clearInterval(progressInterval);
    isGenerating.value = false;
    progress.value = 0;
  }
};

// Edit image function (for Edit Image)
const editImage = async () => {
  if (!uploadedImageFile.value || !editImagePrompt.value.trim() || isGenerating.value) {
    return;
  }

  isGenerating.value = true;
  errorMessage.value = '';
  progress.value = 0;
  generatedImage.value = null;

  const progressInterval = setInterval(() => {
    if (progress.value < 90) {
      progress.value += Math.random() * 10;
    }
  }, 500);

  const formData = new FormData();
  formData.append('image', uploadedImageFile.value);
  formData.append('prompt', editImagePrompt.value);

  try {
    const response = await fetch(`/api/edit-image`, {
      method: 'POST',
      body: formData
    });

    const data = await response.json();

    if (response.ok && data.success) {
      generatedImage.value = `${API_BASE_URL}${data.imageUrl}`;
      credits.value = Math.max(0, credits.value - 4); // Assuming editing also costs credits
      progress.value = 100;
    } else {
      throw new Error(data.error || 'Image editing failed');
    }
  } catch (error) {
    console.error('Error editing image:', error);
    errorMessage.value = error.message || '编辑图片时发生错误，请重试';
  } finally {
    clearInterval(progressInterval);
    isGenerating.value = false;
    progress.value = 0;
  }
};

// Regenerate image (based on active tool)
const regenerateImage = () => {
  if (activeTool.value === 'Text to Image') {
    generateImage();
  } else if (activeTool.value === 'Edit Image') {
    editImage();
  }
};

// Download image
const downloadImage = () => {
  if (generatedImage.value) {
    const link = document.createElement('a');
    link.href = generatedImage.value;
    link.download = `generated-image-${Date.now()}.png`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }
};

// Export image
const exportImage = () => {
  downloadImage();
};

// Check API health on mount
onMounted(async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/health`);
    if (!response.ok) {
      errorMessage.value = 'API服务器连接失败，请确保后端服务正在运行';
    }
  } catch (error) {
    errorMessage.value = 'API服务器连接失败，请确保后端服务正在运行';
  }
});
</script>

<style scoped>
/* Main Layout */
.editor-layout {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: #0e0e0e;
  color: #ffffff;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Top Navigation */
.top-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 56px;
  padding: 0 1rem;
  background-color: #1a1a1a;
  border-bottom: 1px solid #222;
}

.left-controls,
.center-controls,
.right-controls {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.home-button {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  background-color: transparent;
  border: none;
  color: #ccc;
  cursor: pointer;
}

.document-info {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #ccc;
  font-size: 0.9rem;
}

.doc-title {
  font-weight: 500;
}

.doc-size {
  color: #888;
}

.tool-button {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  background-color: transparent;
  border: none;
  color: #ccc;
  cursor: pointer;
  transition: all 0.2s ease;
}

.tool-button:hover {
  background-color: #333;
  color: #fff;
}

.tool-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.play-button {
  background-color: #D4AF37;
  color: #000;
}

.play-button:hover:not(:disabled) {
  background-color: #e6c34a;
}

.credits {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  padding: 0.5rem;
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 6px;
  color: #ccc;
  font-size: 0.9rem;
}

.export-button {
  padding: 0.5rem 1rem;
  background-color: transparent;
  border: 1px solid #444;
  border-radius: 6px;
  color: #ccc;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.export-button:hover:not(:disabled) {
  background-color: #333;
}

.export-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Editor Container */
.editor-container {
  display: flex;
  flex: 1;
  overflow: hidden;
}

/* Icon Sidebar */
.icon-sidebar {
  width: 70px;
  height: 100%;
  display: flex;
  flex-direction: column;
  background-color: #121212;
  border-right: 1px solid #222;
  transition: width 0.3s ease;
}

.icon-sidebar.expanded {
  width: 180px;
}

.sidebar-toggle {
  width: 100%;
  padding: 0.75rem 0;
  background-color: #0a0a0a;
  border: none;
  color: #ccc;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-button {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.25rem;
  padding: 0.75rem 0.5rem;
  background-color: transparent;
  border: none;
  color: #ccc;
  font-size: 0.8rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.icon-button:hover,
.icon-button.active {
  background-color: #1a1a1a;
  color: #fff;
}

/* Tool Panel */
.tool-panel {
  width: 320px;
  height: 100%;
  background-color: #1a1a1a;
  border-right: 1px solid #222;
  overflow-y: auto;
}

.tool-panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border-bottom: 1px solid #222;
}

.tool-panel-header h3 {
  font-size: 1.25rem;
  font-weight: 500;
  margin: 0;
}

.close-panel-btn {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: transparent;
  border: none;
  color: #ccc;
  cursor: pointer;
  border-radius: 6px;
}

.close-panel-btn:hover {
  background-color: #333;
}

.tool-panel-content {
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.model-selector {
  display: flex;
  align-items: center;
  background-color: #222;
  padding: 0.5rem;
  border-radius: 6px;
}

.model-preview {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.model-icon {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
}

.prompt-area {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.prompt-input {
  min-height: 150px;
  background-color: #222;
  border: none;
  border-radius: 6px;
  color: #fff;
  padding: 0.75rem;
  font-family: inherit;
  resize: vertical;
}

.prompt-input:focus {
  outline: 2px solid #D4AF37;
}

.prompt-counter {
  align-self: flex-end;
  font-size: 0.8rem;
  color: #888;
}

.option-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
}

.option-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex: 1;
}

.aspect-value {
  font-size: 0.9rem;
  color: #ccc;
}

.aspect-buttons {
  display: flex;
  gap: 0.5rem;
}

.aspect-button {
  flex: 1;
  padding: 0.5rem 0;
  background-color: #333;
  border: none;
  border-radius: 4px;
  color: #ccc;
  cursor: pointer;
  transition: all 0.2s ease;
}

.aspect-button.active {
  background-color: #444;
  color: #fff;
}

.generation-status {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  padding: 1rem;
  background-color: #222;
  border-radius: 6px;
}

.status-indicator {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.spinner {
  width: 16px;
  height: 16px;
  border: 2px solid #333;
  border-top: 2px solid #D4AF37;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.progress-bar {
  height: 4px;
  background-color: #333;
  border-radius: 2px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background-color: #D4AF37;
  transition: width 0.3s ease;
}

.error-message {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem;
  background-color: #2d1b1b;
  border: 1px solid #d32f2f;
  border-radius: 6px;
  color: #f44336;
  font-size: 0.9rem;
}

.generate-button {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem 1rem;
  background-color: #D4AF37;
  border: none;
  border-radius: 6px;
  color: #000;
  font-weight: 600;
  cursor: pointer;
  margin-top: 1rem;
  transition: all 0.2s ease;
}

.generate-button:hover:not(:disabled) {
  background-color: #e6c34a;
}

.generate-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.generate-label {
  font-size: 0.8rem;
  font-weight: normal;
  background-color: rgba(0, 0, 0, 0.2);
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
}

.credit-amount {
  background-color: #fff;
  color: #000;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
}

/* Upload area specific styles */
.upload-area {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  align-items: flex-start;
}

.upload-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background-color: #333;
  border: 1px solid #444;
  border-radius: 6px;
  color: #fff;
  cursor: pointer;
  transition: all 0.2s ease;
}

.upload-button:hover {
  background-color: #444;
}

.image-upload-preview {
  max-width: 100%;
  max-height: 200px;
  overflow: hidden;
  border-radius: 6px;
  border: 1px solid #222;
}

.image-upload-preview img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}


/* Canvas Area */
.canvas-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  background-color: #121212;
}

.canvas-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  overflow: hidden;
}

.canvas-placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.placeholder-content {
  text-align: center;
  color: #888;
}

.placeholder-icon {
  margin-bottom: 1rem;
  color: #555;
}

.placeholder-content h2 {
  margin: 0 0 0.5rem;
  font-size: 1.5rem;
  color: #ccc;
}

.placeholder-content p {
  margin: 0;
  font-size: 1rem;
}

.generation-preview {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.generation-placeholder {
  text-align: center;
  max-width: 400px;
}

.generation-spinner {
  margin-bottom: 1.5rem;
}

.spinner-ring {
  width: 60px;
  height: 60px;
  border: 4px solid #333;
  border-top: 4px solid #D4AF37;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto;
}

.generation-placeholder h3 {
  margin: 0 0 0.5rem;
  color: #D4AF37;
}

.generation-placeholder p {
  margin: 0;
  color: #888;
  font-style: italic;
}

.image-result {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  max-width: 100%;
  max-height: 100%;
}

.generated-image {
  max-width: 100%;
  max-height: calc(100vh - 200px);
  object-fit: contain;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.image-actions {
  display: flex;
  gap: 0.5rem;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background-color: #333;
  border: none;
  border-radius: 6px;
  color: #fff;
  cursor: pointer;
  transition: all 0.2s ease;
}

.action-btn:hover {
  background-color: #444;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

.animate-spin {
  animation: spin 1s linear infinite;
}

/* Responsive */
@media (max-width: 768px) {
  .tool-panel {
    width: 280px;
  }

  .canvas-content {
    padding: 1rem;
  }
}
</style>
