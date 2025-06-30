<template>
  <div class="app">
    <nav class="navbar">
      <div class="navbar-left">
        <a href="#" class="logo">
          siyan<span class="beta">BETA</span>
        </a>

        <div class="nav-links">
          <div class="dropdown">
            <button class="dropdown-btn">
              Tools <span class="dropdown-arrow">▼</span>
            </button>
          </div>

          <div class="dropdown">
            <button class="dropdown-btn">
              Resources <span class="dropdown-arrow">▼</span>
            </button>
          </div>

          <a href="#pricing" class="nav-link">Pricing</a>
          <a href="#api" class="nav-link">API</a>
          <a href="#contact" class="nav-link">Contact Sales</a>
          <a href="#demo" class="nav-link">Book a Demo</a>
        </div>
      </div>

      <div class="navbar-right">
        <div id="g_id_onload"
             data-client_id="682733356459-dicd4vmvs2nrfuqcv6qtmeja3vei8suu.apps.googleusercontent.com"
             data-context="signin"
             data-ux_mode="popup"
             data-callback="handleCredentialResponse"
             data-auto_select="true"
             data-itp_support="true"
             data-locale="en"> </div>

        <div class="g_id_signin google-login-desktop"
             data-type="standard"
             data-shape="pill"
             data-theme="outline"
             data-text="signin_with"
             data-size="large"
             data-logo_alignment="left">
        </div>
        <button class="btn-primary">Start for Free</button>
      </div>

      <button class="mobile-menu-btn" @click="mobileMenuOpen = !mobileMenuOpen">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </nav>

    <div class="mobile-menu" :class="{ 'open': mobileMenuOpen }">
      <a href="#" class="mobile-link">Tools</a>
      <a href="#" class="mobile-link">Resources</a>
      <a href="#pricing" class="mobile-link">Pricing</a>
      <a href="#api" class="mobile-link">API</a>
      <a href="#contact" class="mobile-link">Contact Sales</a>
      <a href="#demo" class="mobile-link">Book a Demo</a>
      <div id="g_id_onload_mobile"
           data-client_id="682733356459-dicd4vmvs2nrfuqcv6qtmeja3vei8suu.apps.googleusercontent.com"
           data-context="signin"
           data-ux_mode="popup"
           data-callback="handleCredentialResponse"
           data-auto_select="true"
           data-itp_support="true"
           data-locale="en"> </div>

      <div class="g_id_signin google-login-mobile"
           data-type="standard"
           data-shape="pill"
           data-theme="outline"
           data-text="signin_with"
           data-size="large"
           data-logo_alignment="left">
      </div>
      <button class="btn-primary mobile-btn">Start for Free</button>
    </div>

    <section class="hero">
      <div class="container">
        <h1 class="hero-title">
          One Subscription for All<br>
          AI Visual Tools
        </h1>
        <p class="hero-subtitle">
          Save Time and Money: No More Switching Between Expensive AI Design Apps
        </p>
        <button class="hero-button">
          Start for <strong>FREE</strong> today
        </button>
      </div>
    </section>

    <section class="tools-grid">
      <div class="container">
        <div class="tools-container">
          <div class="tool-card tool-image-to-image">
            <div class="tool-header">
              <div class="tool-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect width="18" height="18" x="3" y="3" rx="2" />
                  <circle cx="9" cy="9" r="2" />
                  <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21" />
                </svg>
              </div>
              <h3 class="tool-name">Image-to-Image</h3>
            </div>
            <div class="tool-content">
              <div class="demo-container">
                <div class="before-image">
                  <span class="tag">Before</span>
                  <img src="https://static.dzine.ai/tools/dashboard/ai-tools-cover/image-to-image.png" alt="Sketch">
                </div>
                <div class="transform-arrow">
                  <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none"
                    stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
                    <path d="M15 3h6v6" />
                    <path d="m10 14 11-11" />
                  </svg>
                </div>
                <div class="after-image">
                  <span class="tag">After</span>
                  <img src="https://static.dzine.ai/tools/dashboard/ai-tools-cover/image-to-image.png"
                    alt="Generated Photo">
                </div>
              </div>
            </div>
          </div>

          <div class="tool-card tool-text-to-image">
            <div class="tool-header">
              <div class="tool-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M4 7V4h16v3" />
                  <path d="M9 20h6" />
                  <path d="M12 4v16" />
                </svg>
              </div>
              <h3 class="tool-name">Text-to-Image</h3>
            </div>
            <div class="tool-content">
              <div class="demo-container">
                <div class="text-prompt">
                  <p>Delicious Fried<br>Cheese Stuffed<br>Doritos</p>
                </div>
                <div class="transform-arrow">
                  <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none"
                    stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
                    <path d="M15 3h6v6" />
                    <path d="m10 14 11-11" />
                  </svg>
                </div>
                <div class="generated-image">
                  <img src="https://static.dzine.ai/tools/dashboard/ai-tools-cover/text-to-image.png"
                    alt="Generated Food">
                </div>
              </div>
            </div>
          </div>

          <div class="tool-card tool-consistent-character">
            <div class="tool-header">
              <div class="tool-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="8" r="5" />
                  <path d="M20 21v-2a5 5 0 0 0-5-5h-6a5 5 0 0 0-5 5v2" />
                </svg>
              </div>
              <h3 class="tool-name">Consistent Character</h3>
            </div>
            <div class="tool-content">
              <div class="character-grid">
                <img src="https://static.dzine.ai/tools/dashboard/ai-tools-cover/consistent-character.png"
                  alt="Character 1">
                <img src="https://static.dzine.ai/tools/dashboard/ai-tools-cover/consistent-character.png"
                  alt="Character 2">
                <img src="https://static.dzine.ai/tools/dashboard/ai-tools-cover/consistent-character.png"
                  alt="Character 3">
                <img src="https://static.dzine.ai/tools/dashboard/ai-tools-cover/consistent-character.png"
                  alt="Character 4">
              </div>
            </div>
          </div>

          <div class="tool-card tool-image-to-video">
            <div class="tool-header">
              <div class="tool-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="m22 8-6 4 6 4V8Z" />
                  <rect width="14" height="12" x="2" y="6" rx="2" ry="2" />
                </svg>
              </div>
              <h3 class="tool-name">Image-to-Video</h3>
            </div>
            <div class="tool-content">
              <div class="video-demo">
                <div class="video-preview">
                  <img src="https://static.dzine.ai/tools/dashboard/ai-tools-cover/image-to-video.png"
                    alt="Video Preview">
                  <div class="play-button">
                    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="white"
                      stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <circle cx="12" cy="12" r="10" />
                      <polygon points="10 8 16 12 10 16 10 8" fill="white" />
                    </svg>
                  </div>
                </div>
                <div class="video-frames">
                  <img src="https://placeholder.pics/svg/200x60/CCCCCC/666666-CCCCCC/frames" alt="Video Frames">
                </div>
              </div>
            </div>
          </div>

          <div class="tool-card tool-insert-object">
            <div class="tool-header">
              <div class="tool-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10" stroke-dasharray="4 4" />
                  <line x1="12" y1="8" x2="12" y2="16" />
                  <line x1="8" y1="12" x2="16" y2="12" />
                </svg>
              </div>
              <h3 class="tool-name">Insert Object</h3>
            </div>
            <div class="tool-content">
              <div class="demo-container">
                <div class="before-image">
                  <img src="https://static.dzine.ai/tools/dashboard/ai-tools-cover/insert-object.png" alt="Dog">
                </div>
                <div class="transform-arrow">
                  <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none"
                    stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
                    <path d="M15 3h6v6" />
                    <path d="m10 14 11-11" />
                  </svg>
                </div>

                <div class="after-image">
                  <img src="https://static.dzine.ai/tools/dashboard/ai-tools-cover/insert-object.png"
                    alt="Dog with Hat">
                </div>
              </div>
            </div>
          </div>

          <div class="tool-card tool-ai-eraser">
            <div class="tool-header">
              <div class="tool-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="m20 20-6-6m2-4a4 4 0 1 1-8 0 4 4 0 0 1 8 0Z" />
                </svg>
              </div>
              <h3 class="tool-name">AI Eraser</h3>
            </div>
            <div class="tool-content">
              <div class="eraser-demo">
                <img src="https://static.dzine.ai/tools/dashboard/ai-tools-cover/ai-eraser.png" alt="Dog with Eraser">
                <div class="eraser-circle">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                    stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M3 3h18v18H3z" />
                    <path d="M15 9h.01M9 15h.01" />
                    <path d="m15 15-6-6" />
                  </svg>
                </div>
              </div>
            </div>
          </div>

          <div class="tool-card tool-expand">
            <div class="tool-header">
              <div class="tool-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M15 3h6v6" />
                  <path d="M9 21H3v-6" />
                  <path d="m21 3-7 7" />
                  <path d="m3 21 7-7" />
                </svg>
              </div>
              <h3 class="tool-name">Expand</h3>
            </div>
            <div class="tool-content">
              <div class="expand-demo">
                <img src="https://static.dzine.ai/tools/dashboard/ai-tools-cover/expand.png" alt="Portrait">
                <div class="expand-arrows">
                  <div class="arrow left">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                      stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="m15 18-6-6 6-6" />
                    </svg>
                  </div>
                  <div class="arrow right">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                      stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="m9 18 6-6-6-6" />
                    </svg>
                  </div>
                  <div class="corner top-left"></div>
                  <div class="corner top-right"></div>
                  <div class="corner bottom-left"></div>
                  <div class="corner bottom-right"></div>
                </div>
              </div>
            </div>
          </div>

          <div class="tool-card tool-enhance">
            <div class="tool-header">
              <div class="tool-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="m2 12 5.25 5 2-2-5.3-5.3a1 1 0 0 0-1.4 0l-.55.6a1 1 0 0 0 0 1.7Z" />
                  <path d="M15 12 9 6l-2 2 6 6 2-2Z" />
                  <path
                    d="m22 12-5.3-5.3a1 1 0 0 0-1.4 0l-5.3 5.3 2 2 5.25-5 4.25 4a1 1 0 0 0 1.4-.3l.6-.5a1 1 0 0 0-.5-1.2Z" />
                </svg>
              </div>
              <h3 class="tool-name">Enhance</h3>
            </div>
            <div class="tool-content">
              <div class="enhance-demo">
                <div class="split-image">
                  <img src="https://static.dzine.ai/tools/dashboard/ai-tools-cover/enhance.png"
                    alt="Pixelated vs Enhanced">
                  <div class="split-line"></div>
                </div>
              </div>
            </div>
          </div>
        </div>


      </div>
    </section>

    <section class="hero">
      <h1 class="hero-title">
        All-In-One<br />
        AI Design Platform
      </h1>
      <p class="hero-subtitle">
        Generate and edit in one place with AI-Powered design workflow.
      </p>
    </section>
    <div class="feature-sections">
      <section class="feature-section">
        <div class="feature-container">
          <div class="feature-image">
            <video class="vi" poster="https://static.dzine.ai/assets/pre_load-dz-800-400.jpeg" playsinline=""
              autoplay="" loop="" muted="" data-v-5f31b5ed="">
              <source src="https://static.dzine.ai/videos/AI%2BPhoto%2BFilter1.mp4" type="video/mp4" data-v-5f31b5ed="">
            </video>

          </div>
          <div class="feature-content">
            <h2 class="feature-title">AI Photo Filter</h2>
            <p class="feature-description">
              Transform your portrait or photo to cartoon with our <strong>AI Filter</strong>. siyan (formerly Stylar
              AI) makes it easy to keep your photo details and characters in generative art.
            </p>
            <a href="#" class="feature-button">Transform your photo style</a>
          </div>
        </div>
      </section>

      <section class="feature-section feature-section-reverse">
        <div class="feature-container">
          <div class="feature-image feature-image-colored">
            <video class="vi" poster="https://static.dzine.ai/assets/pre_load-dz-800-400.jpeg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="https://static.dzine.ai/videos/Combine+Images+with+AI.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">Combine Images with AI</h2>
            <p class="feature-description">
              Generatively merge different elements into one complete image, and make them all match in style. siyan
              (formerly Stylar AI) offers the best <strong>AI Image Combiner</strong> in the world.
            </p>
            <a href="#" class="feature-button">Mix your images</a>
          </div>

        </div>
      </section>

      <section class="feature-section">
        <div class="feature-container">
          <div class="feature-image">
            <video class="vi" poster="https://static.dzine.ai/assets/pre_load-dz-800-400.jpeg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="https://static.dzine.ai/videos/Remove+Background.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">AI Background Removal</h2>
            <p class="feature-description">
              Remove backgrounds from your images with perfect precision using our <strong>AI Background
                Remover</strong>. siyan (formerly Stylar AI) preserves fine details like hair and transparent elements.
            </p>
            <a href="#" class="feature-button">Remove backgrounds instantly</a>
          </div>
        </div>
      </section>

      <section class="feature-section feature-section-reverse">
        <div class="feature-container">
          <div class="feature-image feature-image-colored" style="--feature-bg-color: #D1C4E9;">
            <video class="vi" poster="https://static.dzine.ai/assets/pre_load-dz-800-400.jpeg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="https://static.dzine.ai/videos/Remove+Background.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">AI Image Enhancer</h2>
            <p class="feature-description">
              Transform low-quality images into crystal-clear, high-resolution visuals with our <strong>AI Image
                Enhancer</strong>. siyan (formerly Stylar AI) uses advanced upscaling technology to restore details.
            </p>
            <a href="#" class="feature-button">Enhance your images</a>
          </div>

        </div>
      </section>

      <section class="feature-section">
        <div class="feature-container">
          <div class="feature-image">
            <video class="vi" poster="https://static.dzine.ai/assets/pre_load-dz-800-400.jpeg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="https://static.dzine.ai/videos/text-effect-logo-1.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">AI Text to Image</h2>
            <p class="feature-description">
              Turn your ideas into stunning visuals with just a text prompt. Our <strong>AI Text to Image</strong>
              generator creates unique, high-quality images that match your descriptions perfectly.
            </p>
            <a href="#" class="feature-button">Generate from text</a>
          </div>
        </div>
      </section>

      <section class="feature-section feature-section-reverse">
        <div class="feature-container">
          <div class="feature-image feature-image-colored" style="--feature-bg-color: #BBDEFB;">
            <video class="vi" poster="https://static.dzine.ai/assets/pre_load-dz-800-400.jpeg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="https://static.dzine.ai/videos/generative-object-1.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">AI Image Expansion</h2>
            <p class="feature-description">
              Expand your images beyond their original boundaries with our <strong>AI Image Expansion</strong> tool.
              siyan (formerly Stylar AI) seamlessly extends your images while maintaining visual consistency.
            </p>
            <a href="#" class="feature-button">Expand your canvas</a>
          </div>

        </div>
      </section>
    </div>
    <section class="features">
      <h2 class="section-title">Why Choose siyan.ai?</h2>

      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
              stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
              class="lucide lucide-zap">
              <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
            </svg>
          </div>
          <h3 class="feature-title">Lightning Fast</h3>
          <p class="feature-description">Generate high-quality visuals in seconds, not minutes or hours</p>
        </div>

        <div class="feature-card">
          <div class="feature-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
              stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
              class="lucide lucide-sparkles">
              <path
                d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z">
              </path>
              <path d="M5 3v4"></path>
              <path d="M19 17v4"></path>
              <path d="M3 5h4"></path>
              <path d="M17 19h4"></path>
            </svg>
          </div>
          <h3 class="feature-title">Professional Quality</h3>
          <p class="feature-description">Create studio-quality visuals without professional skills</p>
        </div>

        <div class="feature-card">
          <div class="feature-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
              stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
              class="lucide lucide-wallet">
              <path d="M21 12V7H5a2 2 0 0 1 0-4h14v4"></path>
              <path d="M3 5v14a2 2 0 0 0 2 2h16v-5"></path>
              <path d="M18 12a2 2 0 0 0 0 4h4v-4Z"></path>
            </svg>
          </div>
          <h3 class="feature-title">Cost Effective</h3>
          <p class="feature-description">One subscription for all tools, saving you hundreds of dollars</p>
        </div>
      </div>
    </section>

    <section id="pricing" class="pricing">
      <h2 class="section-title">Simple, Transparent Pricing</h2>
      <p class="section-subtitle">Choose the plan that works for you</p>

      <div class="pricing-grid">
        <div class="pricing-card">
          <div class="pricing-header">
            <h3 class="pricing-title">Basic</h3>
            <div class="pricing-price">
              <span class="price">$19</span>
              <span class="period">/month</span>
            </div>
          </div>
          <ul class="pricing-features">
            <li>5 AI generations per day</li>
            <li>Access to basic tools</li>
            <li>720p resolution</li>
            <li>Email support</li>
          </ul>
          <button class="btn-secondary">Get Started</button>
        </div>

        <div class="pricing-card featured">
          <div class="pricing-badge">Popular</div>
          <div class="pricing-header">
            <h3 class="pricing-title">Pro</h3>
            <div class="pricing-price">
              <span class="price">$49</span>
              <span class="period">/month</span>
            </div>
          </div>
          <ul class="pricing-features">
            <li>50 AI generations per day</li>
            <li>Access to all tools</li>
            <li>4K resolution</li>
            <li>Priority support</li>
            <li>Commercial usage</li>
          </ul>
          <button class="btn-primary">Get Started</button>
        </div>

        <div class="pricing-card">
          <div class="pricing-header">
            <h3 class="pricing-title">Enterprise</h3>
            <div class="pricing-price">
              <span class="price">Custom</span>
            </div>
          </div>
          <ul class="pricing-features">
            <li>Unlimited AI generations</li>
            <li>Access to all tools + API</li>
            <li>8K resolution</li>
            <li>Dedicated support</li>
            <li>Custom integrations</li>
            <li>Team management</li>
          </ul>
          <button class="btn-secondary">Contact Sales</button>
        </div>
      </div>
    </section>
    <section class="use-cases-section">
      <div class="container">
        <h2 class="use-cases-title">Best Ways to Use siyan AI Image Editor</h2>
        <p class="use-cases-subtitle">What do the pros create with siyan (formerly Stylar AI)?</p>

        <div class="use-cases-tabs">
          <button v-for="(tab, index) in tabs" :key="index" :class="['tab-button', { active: activeTab === index }]"
            @click="setActiveTab(index)">
            {{ tab.name }}
          </button>
        </div>

        <div class="use-cases-content">
          <div class="content-left">
            <h3 class="content-title">{{ tabs[activeTab].title }}</h3>
            <p class="content-description">{{ tabs[activeTab].description }}</p>
          </div>

          <div class="content-right">
            <div class="image-carousel">
              <div class="carousel-images" :style="{ transform: `translateX(-${activeImageIndex * 100}%)` }">
                <img v-for="(image, index) in tabs[activeTab].images" :key="index" :src="image"
                  :alt="`${tabs[activeTab].name} example ${index + 1}`" class="carousel-image" />
              </div>

              <div class="carousel-controls" v-if="tabs[activeTab].images.length > 1">
                <button class="control-button prev" @click="prevImage" :disabled="activeImageIndex === 0">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                    stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M15 18l-6-6 6-6" />
                  </svg>
                </button>
                <div class="carousel-dots">
                  <button v-for="(_, index) in tabs[activeTab].images" :key="index"
                    :class="['dot', { active: activeImageIndex === index }]" @click="setActiveImage(index)"></button>
                </div>
                <button class="control-button next" @click="nextImage"
                  :disabled="activeImageIndex === tabs[activeTab].images.length - 1">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                    stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M9 18l6-6-6-6" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="testimonials">
      <h2 class="section-title">What Our Users Say</h2>

      <div class="testimonials-grid">
        <div class="testimonial-card">
          <div class="testimonial-content">
            "siyan.ai has completely transformed our creative workflow. We're producing content in minutes that used to
            take hours."
          </div>
          <div class="testimonial-author">
            <div class="testimonial-avatar"></div>
            <div class="testimonial-info">
              <div class="testimonial-name">Sarah Johnson</div>
              <div class="testimonial-role">Marketing Director</div>
            </div>
          </div>
        </div>

        <div class="testimonial-card">
          <div class="testimonial-content">
            "The quality of images I can create with siyan.ai is incredible. It's like having a professional designer on
            call 24/7."
          </div>
          <div class="testimonial-author">
            <div class="testimonial-avatar"></div>
            <div class="testimonial-info">
              <div class="testimonial-name">Michael Chen</div>
              <div class="testimonial-role">E-commerce Entrepreneur</div>
            </div>
          </div>
        </div>

        <div class="testimonial-card">
          <div class="testimonial-content">
            "We've cut our design costs by 70% while increasing our output. The ROI with siyan.ai is simply unmatched."
          </div>
          <div class="testimonial-author">
            <div class="testimonial-avatar"></div>
            <div class="testimonial-info">
              <div class="testimonial-name">Alex Rivera</div>
              <div class="testimonial-role">Creative Director</div>
            </div>
          </div>
        </div>
      </div>
    </section>



    <section class="cta">
      <h2 class="cta-title">Ready to Transform Your Visual Content?</h2>
      <p class="cta-subtitle">Join thousands of creators and businesses using siyan.ai today</p>
      <button class="btn-primary btn-large">Start Creating for Free</button>
      <p class="cta-note">No credit card required</p>
    </section>

    <div class="pre-footer">
      <div class="container">
        <h2 class="pre-footer-title">Create Your First Project in siyan</h2>
        <button class="btn-primary btn-large">Start for Free</button>
      </div>
    </div>

    <footer class="new-footer">
      <div class="container">
        <div class="footer-top">
          <div class="footer-brand">
            <a href="#" class="footer-logo">
              <span class="logo-text">siyan</span>
              <span class="logo-beta">BETA</span>
            </a>
            <p class="footer-tagline">
              Controllable AI Image Editing &<br>
              Graphic Design Tool for Everyone
            </p>
            <div class="footer-social">
              <a href="#" class="social-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path
                    d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z">
                  </path>
                </svg>
              </a>
              <a href="#" class="social-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect width="20" height="20" x="2" y="2" rx="5" ry="5"></rect>
                  <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                  <line x1="17.5" x2="17.51" y1="6.5" y2="6.5"></line>
                </svg>
              </a>
              <a href="#" class="social-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path
                    d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z">
                  </path>
                  <polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon>
                </svg>
              </a>
              <a href="#" class="social-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                  <rect width="4" height="12" x="2" y="9"></rect>
                  <circle cx="4" cy="4" r="2"></circle>
                </svg>
              </a>
              <a href="#" class="social-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"></circle>
                  <path d="M14.5 9a3.5 3.5 0 0 0-5 0"></path>
                  <path d="M9 12a3 3 0 0 0 6 0"></path>
                  <path d="M14.5 15a3.5 3.5 0 0 0-5 0"></path>
                </svg>
              </a>
            </div>
          </div>
          <div class="footer-links-section">
            <div class="footer-links-column">
              <h3 class="footer-column-title">AI PHOTO FILTER</h3>
              <ul class="footer-links">
                <li><a href="#">2D to 3D Converter</a></li>
                <li><a href="#">AI Design Sketch</a></li>
                <li><a href="#">Image to Prompt</a></li>
                <li><a href="#">AI Style Transfer</a></li>
                <li><a href="#">Turn Sketch to Art</a></li>
                <li><a href="#">AI Anime Filter</a></li>
                <li><a href="#">All Tools</a></li>
              </ul>
            </div>
            <div class="footer-links-column">
              <h3 class="footer-column-title">AI IMAGE EDITOR</h3>
              <ul class="footer-links">
                <li><a href="#">Add Object into Image</a></li>
                <li><a href="#">Remove Object from Image</a></li>
                <li><a href="#">Remove Background</a></li>
                <li><a href="#">AI Combine Images</a></li>
                <li><a href="#">AI Photo Enhancer</a></li>
                <li><a href="#">AI Photo Expand</a></li>
                <li><a href="#">Vectorize Image</a></li>
                <li><a href="#">Insert Object</a></li>
              </ul>
            </div>
            <div class="footer-links-column">
              <h3 class="footer-column-title">AI ART GENERATOR</h3>
              <ul class="footer-links">
                <li><a href="#">AI Character Generator</a></li>
                <li><a href="#">AI Anime Generator</a></li>
                <li><a href="#">AI Comic Generator</a></li>
                <li><a href="#">Flux.1 AI Image Generator</a></li>
                <li><a href="#">AI Coloring Book Generator</a></li>
                <li><a href="#">AI Vector Image Generator</a></li>
                <li><a href="#">AI Product Background Generator</a></li>
              </ul>
            </div>
            <div class="footer-links-column">
              <h3 class="footer-column-title">RESOURCES</h3>
              <ul class="footer-links">
                <li><a href="#">Blog</a></li>
                <li><a href="#">Tutorial</a></li>
                <li><a href="#">Affiliate Program</a></li>
                <li><a href="#">Educator Program</a></li>
                <li><a href="#">FAQ</a></li>
              </ul>
            </div>
            <div class="footer-links-column">
              <h3 class="footer-column-title">Company</h3>
              <ul class="footer-links">
                <li><a href="#">About Us</a></li>
                <li><a href="#">Careers</a></li>
                <li><a href="#">Terms of Service</a></li>
                <li><a href="#">Privacy Policy</a></li>
              </ul>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <p class="footer-copyright">
            © 2024 siyan.ai All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  data() {
    return {
      mobileMenuOpen: false,
      activeTab: 0,
      activeImageIndex: 0,
      tabs: [
        {
          name: 'Social Media',
          title: 'AI Art for Social Media',
          description: 'Create eye-catching social media posts and stories with AI. Generate unique images that stand out and engage your audience.',
          images: [
            'https://static.dzine.ai/assets/use_case_social_media1.png',
            'https://static.dzine.ai/assets/use_case_social_media2.png',
            'https://static.dzine.ai/assets/use_case_social_media3.png',
          ]
        },
        {
          name: 'E-commerce',
          title: 'AI Product Photography',
          description: 'Generate stunning product images for your e-commerce store. Create professional-grade visuals without the need for expensive photoshoots.',
          images: [
            'https://static.dzine.ai/assets/use_case_ecommerce1.png',
            'https://static.dzine.ai/assets/use_case_ecommerce2.png',
            'https://static.dzine.ai/assets/use_case_ecommerce3.png',
          ]
        },
        {
          name: 'Marketing',
          title: 'AI for Marketing Campaigns',
          description: 'Design compelling visuals for your marketing campaigns. From ads to brochures, generate creative assets that capture attention.',
          images: [
            'https://static.dzine.ai/assets/use_case_marketing1.png',
            'https://static.dzine.ai/assets/use_case_marketing2.png',
            'https://static.dzine.ai/assets/use_case_marketing3.png',
          ]
        },
        {
          name: 'Gaming',
          title: 'AI Art for Game Development',
          description: 'Produce unique characters, environments, and assets for your games with AI. Accelerate your game development workflow.',
          images: [
            'https://static.dzine.ai/assets/use_case_gaming1.png',
            'https://static.dzine.ai/assets/use_case_gaming2.png',
            'https://static.dzine.ai/assets/use_case_gaming3.png',
          ]
        },
      ]
    };
  },
  mounted() {
    // Load Google Identity Services library
    const script = document.createElement('script');
    script.src = 'https://accounts.google.com/gsi/client';
    script.async = true;
    script.defer = true;
    document.head.appendChild(script);

    // Make the Vue method globally accessible for the Google callback
    window.handleCredentialResponse = this.handleCredentialResponse;
  },
  methods: {
    handleCredentialResponse(response) {
      const jwt = response.credential;
      const userInfoUrl = 'https://aidraw.maiiepay.com/api/login?credential=' + encodeURIComponent(jwt);
      fetch(userInfoUrl)
        .then(res => res.json())
        .then(data => {
          console.log('登录成功:', data);
          // Handle successful login, e.g., redirect or update UI
        })
        .catch(error => {
          console.error('登录失败:', error);
        });
    },
    setActiveTab(index) {
      this.activeTab = index;
      this.activeImageIndex = 0; // Reset image index when tab changes
    },
    prevImage() {
      if (this.activeImageIndex > 0) {
        this.activeImageIndex--;
      }
    },
    nextImage() {
      if (this.activeImageIndex < this.tabs[this.activeTab].images.length - 1) {
        this.activeImageIndex++;
      }
    },
  },
};
</script>

<style>
/* Your existing styles here */

/* Styling for the Google Sign-In button */
.google-login-desktop {
  margin-right: 10px;
  padding: 3px;
  transform: scale(0.8);
}

/* Ensure navbar-right uses flexbox for alignment if it doesn't already */
.navbar-right {
  display: flex;
  align-items: center; /* Vertically align items */
}

/* Styles for mobile menu Google button if different spacing is needed */
.mobile-menu .google-login-mobile {
  margin-bottom: 10px; /* Example: add bottom margin for mobile button */
}

/* Adjust btn-primary if its height is too different */
.btn-primary {
  /* Ensure a consistent height if the Google button still looks off */
  /* For example: */
  /* height: 40px; */
  /* line-height: 40px; */
  /* display: flex; */
  /* align-items: center; */
  /* justify-content: center; */
}

</style>
