<template>
  <div class="app">
    <nav class="navbar">
      <div class="navbar-left">
        <a href="#" class="logo">
          Siyan<span class="beta">BETA</span>
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
       
        <div class="language-switcher">
          <select @change="changeLanguage($event.target.value)">
            <option value="en">English</option>
            <option value="zh-cn">中文</option>
            <option value="es">Español</option>
            <option value="pt">Português</option>
          </select>
        </div>

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
                  <img src="/downloaded_images/f6d25e5fbd4162f138ef5ab5ec9429b3.png" alt="Sketch">
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
                  <img src="/downloaded_images/f6d25e5fbd4162f138ef5ab5ec9429b3.png"
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
                  <img src="/downloaded_images/a0b2013e8ce553faf5c9f4e9aad44e8a.png"
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
                <img src="/downloaded_images/aa354bc214271b7bd0891d87e901d4d6.png"
                  alt="Character 1">
                <img src="/downloaded_images/aa354bc214271b7bd0891d87e901d4d6.png"
                  alt="Character 2">
                <img src="/downloaded_images/aa354bc214271b7bd0891d87e901d4d6.png"
                  alt="Character 3">
                <img src="/downloaded_images/aa354bc214271b7bd0891d87e901d4d6.png"
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
                  <img src="/downloaded_images/4a8b43a258734524656cdfed09240624.png"
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
                  <img src="/downloaded_images/165dd59e80dd395e5cb0d6ee989af7c5.jpg" alt="Video Frames">
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
                  <img src="/downloaded_images/5688b96812e55548ca80f2b457759c0e.png" alt="Dog">
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
                  <img src="/downloaded_images/5688b96812e55548ca80f2b457759c0e.png"
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
                <img src="/downloaded_images/572e3ca191d1da1af6aa6fe8f06d3a77.png" alt="Dog with Eraser">
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
                <img src="/downloaded_images/67e97348fd18b7bc4c74c40ec1cf76b8.png" alt="Portrait">
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
                  <img src="/downloaded_images/8fde87c2cd358c1142568b1e96f98fb2.png"
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
            <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline=""
              autoplay="" loop="" muted="" data-v-5f31b5ed="">
              <source src="/downloaded_images/1723d78d1dcdd3f9992ccb137ee22899.mp4" type="video/mp4" data-v-5f31b5ed="">
            </video>

          </div>
          <div class="feature-content">
            <h2 class="feature-title">AI Photo Filter</h2>
            <p class="feature-description">
              Transform your portrait or photo to cartoon with our <strong>AI Filter</strong>. Siyan (formerly Stylar
              AI) makes it easy to keep your photo details and characters in generative art.
            </p>
            <a href="#" class="feature-button">Transform your photo style</a>
          </div>
        </div>
      </section>

      <section class="feature-section feature-section-reverse">
        <div class="feature-container">
          <div class="feature-image feature-image-colored">
            <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="/downloaded_images/007d2cabdc49a60f038ffc7521d68b4d.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">Combine Images with AI</h2>
            <p class="feature-description">
              Generatively merge different elements into one complete image, and make them all match in style. Siyan
              (formerly Stylar AI) offers the best <strong>AI Image Combiner</strong> in the world.
            </p>
            <a href="#" class="feature-button">Mix your images</a>
          </div>

        </div>
      </section>

      <section class="feature-section">
        <div class="feature-container">
          <div class="feature-image">
            <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="/downloaded_images/b9797ecc51e7eae3474d37f804cdd9b7.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">AI Background Removal</h2>
            <p class="feature-description">
              Remove backgrounds from your images with perfect precision using our <strong>AI Background
                Remover</strong>. Siyan (formerly Stylar AI) preserves fine details like hair and transparent elements.
            </p>
            <a href="#" class="feature-button">Remove backgrounds instantly</a>
          </div>
        </div>
      </section>

      <section class="feature-section feature-section-reverse">
        <div class="feature-container">
          <div class="feature-image feature-image-colored" style="--feature-bg-color: #D1C4E9;">
            <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="/downloaded_images/b9797ecc51e7eae3474d37f804cdd9b7.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">AI Image Enhancer</h2>
            <p class="feature-description">
              Transform low-quality images into crystal-clear, high-resolution visuals with our <strong>AI Image
                Enhancer</strong>. Siyan (formerly Stylar AI) uses advanced upscaling technology to restore details.
            </p>
            <a href="#" class="feature-button">Enhance your images</a>
          </div>

        </div>
      </section>

      <section class="feature-section">
        <div class="feature-container">
          <div class="feature-image">
            <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="/downloaded_images/9c84291bb7eb0925593968a200f8ae77.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
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
            <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="/downloaded_images/b4a278ff50a8530ed308f50a0e194638.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">AI Image Expansion</h2>
            <p class="feature-description">
              Expand your images beyond their original boundaries with our <strong>AI Image Expansion</strong> tool.
              Siyan (formerly Stylar AI) seamlessly extends your images while maintaining visual consistency.
            </p>
            <a href="#" class="feature-button">Expand your canvas</a>
          </div>

        </div>
      </section>
    </div>
    <section class="features">
      <h2 class="section-title">Why Choose Siyan.ai?</h2>

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
        <h2 class="use-cases-title">Best Ways to Use Siyan AI Image Editor</h2>
        <p class="use-cases-subtitle">What do the pros create with Siyan (formerly Stylar AI)?</p>

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
            "Siyan.ai has completely transformed our creative workflow. We're producing content in minutes that used to
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
            "The quality of images I can create with Siyan.ai is incredible. It's like having a professional designer on
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
            "We've cut our design costs by 70% while increasing our output. The ROI with Siyan.ai is simply unmatched."
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
      <p class="cta-subtitle">Join thousands of creators and businesses using Siyan.ai today</p>
      <button class="btn-primary btn-large">Start Creating for Free</button>
      <p class="cta-note">No credit card required</p>
    </section>

    <div class="pre-footer">
      <div class="container">
        <h2 class="pre-footer-title">Create Your First Project in Siyan</h2>
        <button class="btn-primary btn-large">Start for Free</button>
      </div>
    </div>

    <footer class="new-footer">
      <div class="container">
        <div class="footer-top">
          <div class="footer-brand">
            <a href="#" class="footer-logo">
              <span class="logo-text">Siyan</span>
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
            © 2024 Siyan.ai All rights reserved.
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
    changeLanguage(lang) {
      console.log('Switching to language:', lang);
      if (lang === 'zh-cn') {
        window.location.href = '/#/cn';
      } else if (lang === 'es') {
        window.location.href = '/#/es.vue';
      } else if (lang === 'pt') {
        window.location.href = '/#/pt.vue';
      } else {
        window.location.href = '/#/';
      }
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

:root {
  --color-background: #000000;
  --color-foreground: #ffffff;
  --color-primary: #f5c518;
  --color-primary-hover: #e6b400;
  --color-secondary: #1a1a1a;
  --color-secondary-hover: #2a2a2a;
  --color-muted: #666666;
  --color-border: #333333;
  --color-green-bg: linear-gradient(to bottom right, #0d3320, #051a10);
  --color-amber-bg: linear-gradient(to bottom right, #3a2e00, #1a1500);
  --color-purple-bg: linear-gradient(to bottom right, #2e0d3a, #15051a);
  --color-blue-bg: linear-gradient(to bottom right, #0d1a3a, #05091a);
  --border-radius: 8px;
  --transition: all 0.3s ease;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

html,
body {
  height: 100%;
  overflow-x: hidden;
  overflow-y: auto;
}

body {
  background-color: var(--color-background);
  color: var(--color-foreground);
  line-height: 1.6;
}

.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
}

.container {
  width: 100%;
  margin: 0 auto;
  padding: 0 2rem;
}

/* Navigation */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  border-bottom: 1px solid var(--color-border);
  position: sticky;
  top: 0;
  background-color: rgba(0, 0, 0, 0.9);
  backdrop-filter: blur(10px);
  z-index: 100;
}

.navbar-left,
.navbar-right {
  display: flex;
  align-items: center;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--color-foreground);
  text-decoration: none;
  margin-right: 2rem;
}

.beta {
  font-size: 0.6rem;
  vertical-align: super;
  color: var(--color-muted);
  margin-left: 2px;
}

.nav-links {
  display: flex;
  gap: 1.5rem;
}

.nav-link {
  color: #fff;
  text-decoration: none;
  transition: var(--transition);
  margin-right: 2rem;
  font-size: 1.2rem;
}

.nav-link:hover {
  color: var(--color-foreground);
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-btn {
  background: none;
  border: none;
  color: #fff;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 4px;
  transition: var(--transition);
}

.dropdown-btn:hover {
  color: var(--color-foreground);
}

.dropdown-arrow {
  font-size: 0.6rem;
}

.btn-primary {
  background-color: var(--color-primary);
  color: #000;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: var(--border-radius);
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition);
}

.btn-primary:hover {
  background-color: var(--color-primary-hover);
}

.btn-secondary {
  background-color: var(--color-secondary);
  color: var(--color-foreground);
  border: 1px solid var(--color-border);
  padding: 0.5rem 1rem;
  border-radius: var(--border-radius);
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition);
}

.btn-secondary:hover {
  background-color: var(--color-secondary-hover);
}

.btn-outline {
  background-color: transparent;
  color: var(--color-foreground);
  border: 1px solid var(--color-border);
  padding: 0.5rem 1rem;
  border-radius: var(--border-radius);
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition);
}

.btn-outline:hover {
  background-color: var(--color-secondary);
}

.btn-large {
  padding: 0.75rem 1.5rem;
  font-size: 1.1rem;
}

.btn-full {
  width: 100%;
}

.mobile-menu-btn {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
}

.mobile-menu-btn span {
  display: block;
  width: 25px;
  height: 2px;
  background-color: var(--color-foreground);
  margin: 5px 0;
  transition: var(--transition);
}

.mobile-menu {
  display: none;
  position: fixed;
  top: 60px;
  left: 0;
  right: 0;
  background-color: var(--color-background);
  padding: 1rem;
  border-bottom: 1px solid var(--color-border);
  flex-direction: column;
  gap: 10rem;
  transform: translateY(-100%);
  transition: transform 0.3s ease;
  z-index: 99;
}

.mobile-menu.open {
  transform: translateY(0);
}

.mobile-link {
  color: var(--color-muted);
  text-decoration: none;
  padding: 0.5rem 0;
  transition: var(--transition);
}

.mobile-link:hover {
  color: var(--color-foreground);
}

.mobile-btn {
  margin-top: 0.5rem;
}

/* Hero Section */







.bg-green {
  background: var(--color-green-bg);
}

.bg-amber {
  background: var(--color-amber-bg);
}

.bg-purple {
  background: var(--color-purple-bg);
}

.bg-blue {
  background: var(--color-blue-bg);
}


.tool-icon {
  width: 16px;
  height: 16px;
}

.tool-title {
  font-weight: 500;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 2rem;
}

/* Hero Section */
.hero {
  padding: 8rem 0 5rem;
  text-align: center;
  background-color: #000000;
  position: relative;
  overflow: hidden;
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  
  pointer-events: none;
}

.hero-title {
  font-size: 4rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  line-height: 1.2;
  color: #ffffff;
  letter-spacing: 2px
}

.hero-subtitle {
  font-size: 1.5rem;
  color: #9e9e9e;
  max-width: 800px;
  margin: 0 auto 3rem;
}

.hero-button {
  background-color: #f5c518;
  color: #000000;
  border: none;
  padding: 1rem 2.5rem;
  font-size: 1.25rem;
  font-weight: 600;
  border-radius: 2rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.hero-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(245, 197, 24, 0.3);
}

.hero-button strong {
  font-weight: 800;
}

/* Tools Grid */
.tools-grid {
  padding: 3rem 0 6rem;
  background-color: #000000;
  position: relative;
  overflow: hidden;
}

.tools-grid::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(ellipse at center, rgba(245, 197, 24, 0.1) 0%, rgba(0, 0, 0, 0) 70%);
  pointer-events: none;
}

.tools-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.tool-card {
  border-radius: 16px;
  padding: 1.5rem;
  height: 350px;
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
  transition: transform 0.3s ease;
}

.tool-card:hover {
  transform: translateY(-5px);
}

.tool-image-to-image {
  background: linear-gradient(135deg, #291e00 0%, #3a2900 100%);
}

.tool-text-to-image {
  background: linear-gradient(135deg, #3a1700 0%, #4d1d00 100%);
}

.tool-consistent-character {
  background: linear-gradient(135deg, #002a1c 0%, #00402b 100%);
}

.tool-image-to-video {
  background: linear-gradient(135deg, #001a40 0%, #002966 100%);
}

.tool-insert-object {
  background: linear-gradient(135deg, #002a1c 0%, #00402b 100%);
}

.tool-ai-eraser {
  background: linear-gradient(135deg, #002940 0%, #003e66 100%);
}

.tool-expand {
  background: linear-gradient(135deg, #29004d 0%, #3d0073 100%);
}

.tool-enhance {
  background: linear-gradient(135deg, #002a1c 0%, #00402b 100%);
}

.tool-header {
  display: flex;
  align-items: center;
  margin-bottom: 1.5rem;
}

.tool-icon {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 0.75rem;
}

.tool-name {
  font-size: 1.25rem;
  font-weight: 600;
  color: #ffffff;
}

.tool-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Demo Styles */
.demo-container {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.before-image, .after-image, .text-prompt, .generated-image {
  position: relative;
  border-radius: 8px;
  overflow: hidden;
}

.tag {
  position: absolute;
  top: 8px;
  left: 8px;
  background-color: rgba(0, 0, 0, 0.6);
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.75rem;
  z-index: 1;
}

.transform-arrow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: rgba(255, 255, 255, 0.8);
}

.text-prompt {
  background-color: rgba(0, 0, 0, 0.2);
  padding: 1rem;
  border-radius: 8px;
  text-align: left;
}

.text-prompt p {
  margin: 0;
  color: white;
  font-size: 0.9rem;
  line-height: 1.4;
}

.character-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.5rem;
}

.video-demo {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.video-preview {
  position: relative;
  margin-bottom: 1rem;
}

.play-button {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  cursor: pointer;
}

.video-frames {
  border-radius: 8px;
  overflow: hidden;
}

.eraser-demo {
  position: relative;
}

.eraser-circle {
  position: absolute;
  top: 30%;
  left: 50%;
  width: 60px;
  height: 60px;
  border: 2px dashed white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.expand-demo {
  position: relative;
}

.expand-arrows {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.arrow {
  background-color: rgba(0, 0, 0, 0.5);
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.corner {
  position: absolute;
  width: 20px;
  height: 20px;
  border: 2px solid white;
}

.top-left {
  top: 20px;
  left: 20px;
  border-right: none;
  border-bottom: none;
}

.top-right {
  top: 20px;
  right: 20px;
  border-left: none;
  border-bottom: none;
}

.bottom-left {
  bottom: 20px;
  left: 20px;
  border-right: none;
  border-top: none;
}

.bottom-right {
  bottom: 20px;
  right: 20px;
  border-left: none;
  border-top: none;
}

.split-image {
  position: relative;
  border-radius: 8px;
  overflow: hidden;
}

.split-line {
  position: absolute;
  top: 0;
  left: 50%;
  width: 2px;
  height: 100%;
  background-color: white;
}

.next-button {
  position: absolute;
  right: 2rem;
  bottom: 50%;
  transform: translateY(50%);
  width: 48px;
  height: 48px;
  background-color: #f5c518;
  color: #000000;
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  z-index: 10;
}

.next-button:hover {
  transform: translateY(50%) scale(1.1);
}

.small-object {
  position: absolute;
  top: -30px;
  left: 50%;
  transform: translate(-50%, 0);
  z-index: 1;
}

.inserted-object {
  position: relative;
}

/* Responsive Adjustments */
@media (max-width: 1200px) {
  .tools-container {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 992px) {
  .hero-title {
    font-size: 3.5rem;
  }
  
  .tools-container {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 3rem;
  }
  
  .hero-subtitle {
    font-size: 1.25rem;
  }
  
  .tools-container {
    grid-template-columns: 1fr;
  }
  
  .tool-card {
    height: 300px;
  }
}

@media (max-width: 576px) {
  .hero {
    padding: 6rem 0 4rem;
  }
  
  .hero-title {
    font-size: 2.5rem;
  }
  
  .hero-subtitle {
    font-size: 1.1rem;
  }
  
  .hero-button {
    padding: 0.875rem 1.75rem;
    font-size: 1.1rem;
  }
}

.tool-images {
  position: relative;
}

.before-image {
  width: 112px;
  height: 112px;
}

.before-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 4px;
}

.after-image {
  position: absolute;
  right: -16px;
  bottom: -16px;
  width: 112px;
  height: 112px;
}

.after-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 4px;
}

.arrow-icon {
  position: absolute;
  right: 8px;
  top: 50%;
  transform: translateY(-50%);
}

/* Features Section */
.features {
  padding: 4rem 2rem;
  background-color: var(--color-secondary);
  text-align: center;
}

.section-title {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 2rem;
  color: var(--color-foreground);
}

.section-subtitle {
  font-size: 1.25rem;
  color: var(--color-muted);
  margin-bottom: 3rem;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.feature-card {
  padding: 2rem;
  background-color: rgba(255, 255, 255, 0.05);
  border-radius: var(--border-radius);
  transition: var(--transition);
}

.feature-card:hover {
  transform: translateY(-5px);
  background-color: rgba(255, 255, 255, 0.08);
}

.feature-icon {
  width: 48px;
  height: 48px;
  margin: 0 auto 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(245, 197, 24, 0.1);
  border-radius: 50%;
  color: var(--color-primary);
}

.feature-title {
  font-size: 1.25rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.feature-description {
  color: var(--color-muted);
}

/* Pricing Section */
.pricing {
  padding: 4rem 2rem;
  text-align: center;
}

.pricing-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.pricing-card {
  padding: 2rem;
  background-color: var(--color-secondary);
  border-radius: var(--border-radius);
  border: 1px solid var(--color-border);
  transition: var(--transition);
  position: relative;
}

.pricing-card.featured {
  border-color: var(--color-primary);
  transform: scale(1.05);
}

.pricing-badge {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background-color: var(--color-primary);
  color: #000;
  padding: 0.25rem 1rem;
  border-radius: 20px;
  font-weight: 500;
  font-size: 0.875rem;
}

.pricing-header {
  margin-bottom: 2rem;
}

.pricing-title {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.pricing-price {
  font-size: 2.5rem;
  font-weight: bold;
}

.period {
  font-size: 1rem;
  color: var(--color-muted);
  font-weight: normal;
}

.pricing-features {
  list-style: none;
  margin-bottom: 2rem;
  text-align: left;
}

.pricing-features li {
  padding: 0.5rem 0;
  color: var(--color-muted);
}

.pricing-features li::before {
  content: "✓";
  color: var(--color-primary);
  margin-right: 0.5rem;
}

/* Testimonials */
.testimonials {
  padding: 4rem 2rem;
  background-color: var(--color-secondary);
  text-align: center;
}

.testimonials-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.testimonial-card {
  padding: 2rem;
  background-color: rgba(255, 255, 255, 0.05);
  border-radius: var(--border-radius);
  text-align: left;
}

.testimonial-content {
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
  font-style: italic;
}

.testimonial-author {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.testimonial-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: var(--color-muted);
}

.testimonial-name {
  font-weight: 500;
}

.testimonial-role {
  color: var(--color-muted);
  font-size: 0.875rem;
}

/* CTA Section */
.cta {
  padding: 6rem 2rem;
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
}

.cta-title {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.cta-subtitle {
  font-size: 1.25rem;
  color: var(--color-muted);
  margin-bottom: 2rem;
}

.cta-note {
  margin-top: 1rem;
  color: var(--color-muted);
  font-size: 0.875rem;
}

/* Pre-Footer Section */
.pre-footer {
  background-color: var(--color-background);
  padding: 6rem 2rem;
  text-align: center;
  border-bottom: 1px solid var(--color-border);
}

.pre-footer-title {
  font-size: 3.5rem;
  font-weight: bold;
  margin-bottom: 2.5rem;
  color: var(--color-foreground);
}

/* New Footer */
.new-footer {
  background-color: var(--color-background);
  padding: 4rem 0 2rem;
  color: var(--color-foreground);
}

.footer-top {
  display: grid;
  grid-template-columns: 1fr 3fr;
  gap: 3rem;
  margin-bottom: 3rem;
}

.footer-brand {
  display: flex;
  flex-direction: column;
}

.footer-logo {
  display: inline-flex;
  align-items: baseline;
  text-decoration: none;
  margin-bottom: 1rem;
}

.logo-text {
  font-size: 2.5rem;
  font-weight: bold;
  color: var(--color-foreground);
}

.logo-beta {
  font-size: 0.8rem;
  color: var(--color-primary);
  margin-left: 4px;
}

.footer-tagline {
  color: #ffffffb4;
  margin-bottom: 2rem;
  line-height: 1.5;
  text-align: left;
  font-weight: 200;
}

.footer-social {
  display: flex;
  gap: 1rem;
}

.social-icon {
  color: var(--color-muted);
  transition: var(--transition);
}

.social-icon:hover {
  color: var(--color-foreground);
}

.footer-links-section {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 2rem;
  text-align: left;
}

.footer-column-title {
  font-size: 0.8rem;
  font-weight: bold;
  margin-bottom: 1.5rem;
  color: var(--color-primary);
}

.footer-links {
  list-style: none;
}

.footer-links li {
  margin-bottom: 0.25rem;
}

.footer-links a {
  color: #ffffffb4;
  text-decoration: none;
  font-size: 0.9rem;
  transition: var(--transition);
  font-weight: 100;


}

.footer-links a:hover {
  color: var(--color-foreground);
}

.footer-bottom {
  padding-top: 2rem;
  border-top: 1px solid var(--color-border);
}

.copyright {
  color: var(--color-muted);
  font-size: 0.875rem;
}

/* Login Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.7);
  z-index: 1000;
}

.login-modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: var(--color-secondary);
  border-radius: var(--border-radius);
  width: 100%;
  max-width: 450px;
  z-index: 1001;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid var(--color-border);
}

.modal-title {
  font-size: 1.25rem;
  font-weight: bold;
}

.modal-close {
  background: none;
  border: none;
  color: var(--color-muted);
  font-size: 1.5rem;
  cursor: pointer;
  transition: var(--transition);
}

.modal-close:hover {
  color: var(--color-foreground);
}

.modal-body {
  padding: 1.5rem;
}

.login-form {
  margin-bottom: 1.5rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.form-group input {
  width: 100%;
  padding: 0.75rem;
  border-radius: var(--border-radius);
  border: 1px solid var(--color-border);
  background-color: rgba(255, 255, 255, 0.05);
  color: var(--color-foreground);
  transition: var(--transition);
}

.form-group input:focus {
  outline: none;
  border-color: var(--color-primary);
  background-color: rgba(255, 255, 255, 0.1);
}

.password-input {
  position: relative;
}

.password-toggle {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: var(--color-muted);
  cursor: pointer;
  transition: var(--transition);
}

.password-toggle:hover {
  color: var(--color-foreground);
}

.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.checkbox-container {
  display: flex;
  align-items: center;
  cursor: pointer;
  color: var(--color-muted);
  font-size: 0.875rem;
}

.checkbox-container input {
  margin-right: 0.5rem;
}

.forgot-password {
  color: var(--color-primary);
  text-decoration: none;
  font-size: 0.875rem;
  transition: var(--transition);
}

.forgot-password:hover {
  text-decoration: underline;
}

.divider {
  display: flex;
  align-items: center;
  text-align: center;
  margin: 1.5rem 0;
}

.divider::before,
.divider::after {
  content: '';
  flex: 1;
  border-bottom: 1px solid var(--color-border);
}

.divider span {
  padding: 0 10px;
  color: var(--color-muted);
  font-size: 0.875rem;
}

.social-login {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.btn-social {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem;
  border-radius: var(--border-radius);
  border: 1px solid var(--color-border);
  background-color: transparent;
  color: var(--color-foreground);
  cursor: pointer;
  transition: var(--transition);
}

.btn-social:hover {
  background-color: rgba(255, 255, 255, 0.05);
}

.signup-prompt {
  text-align: center;
  color: var(--color-muted);
  font-size: 0.875rem;
}

.signup-prompt a {
  color: var(--color-primary);
  text-decoration: none;
  transition: var(--transition);
}

.signup-prompt a:hover {
  text-decoration: underline;
}

/* Promo Popup */
.promo-popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff1f5;
  border-radius: var(--border-radius);
  width: 100%;
  max-width: 400px;
  z-index: 1001;
  overflow: hidden;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
}

.promo-close {
  position: absolute;
  top: 10px;
  right: 10px;
  background-color: rgba(255, 255, 255, 0.8);
  border: none;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  cursor: pointer;
  z-index: 10;
  transition: var(--transition);
}

.promo-close:hover {
  background-color: rgba(255, 255, 255, 1);
}

.promo-content {
  padding: 2rem;
  text-align: center;
  position: relative;
}

.promo-decoration {
  position: absolute;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background-color: rgba(244, 114, 182, 0.2);
}

.top-right {
  top: -50px;
  right: -50px;
}

.bottom-left {
  bottom: -50px;
  left: -50px;
}

.promo-title {
  color: #f472b6;
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.promo-discount {
  color: #f472b6;
  font-size: 4rem;
  font-weight: bold;
  line-height: 1;
}

.discount-number {
  font-size: 4rem;
}

.discount-percent {
  font-size: 2rem;
  vertical-align: super;
}

.discount-label {
  color: #f472b6;
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.promo-subtitle {
  color: #f472b6;
  margin-bottom: 1.5rem;
}

.promo-code {
  background-color: white;
  border-radius: var(--border-radius);
  padding: 0.75rem;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.code-label {
  color: #666;
}

.code {
  border: 1px solid #f8bbd0;
  border-radius: 4px;
  padding: 0.25rem 0.5rem;
  color: #f472b6;
  font-weight: bold;
}

.promo-note {
  color: #f472b6;
  font-size: 0.875rem;
  margin-bottom: 1.5rem;
}

.promo-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

/* SVG Icons */
[class^="svg-"] {
  display: inline-block;
  width: 16px;
  height: 16px;
}

/* Tool Icons */
.svg-image,
.svg-text,
.svg-user,
.svg-edit,
.svg-plus,
.svg-eraser,
.svg-expand,
.svg-wand,
.svg-bag,
.svg-cube {
  width: 16px;
  height: 16px;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  fill: none;
}

/* Responsive Styles */
@media (max-width: 1200px) {


  .footer-links-section {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 992px) {


  .pricing-grid,
  .features-grid,
  .testimonials-grid {
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  }

  .footer-top {
    grid-template-columns: 1fr;
  }

  .footer-brand {
    margin-bottom: 2rem;
  }

  .footer-links-section {
    grid-template-columns: repeat(2, 1fr);
  }

  .pre-footer-title {
    font-size: 2.5rem;
  }
}

@media (max-width: 768px) {
  .nav-links {
    display: none;
  }

  .mobile-menu-btn {
    display: block;
  }

  .mobile-menu {
    display: flex;
  }




  .section-title {
    font-size: 2rem;
  }

  .pricing-card.featured {
    transform: none;
  }

  .footer-links-section {
    grid-template-columns: 1fr;
  }

  .footer-bottom {
    flex-direction: column;
    gap: 1rem;
  }



  .pre-footer-title {
    font-size: 2rem;
  }
}

@media (max-width: 576px) {
  .navbar {
    padding: 1rem;
  }


  .features,
  .pricing,
  .testimonials,
  .cta,
  .pre-footer {
    padding: 3rem 1rem;
  }



 

  .login-modal {
    width: 90%;
  }

  .promo-popup {
    width: 90%;
  }

  .btn-social {
    font-size: 0.875rem;
  }

  .footer-links-section {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .footer-column-title {
    margin-bottom: 1rem;
  }
}

/* Accessibility Improvements */
:focus {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.use-cases-section {
  padding: 5rem 0;
  background-color: #000000;
  color: #ffffff;
}

.container {

  margin: 0 auto;
  padding: 0 5rem;
}

.use-cases-title {
  font-size: 3.5rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 0.5rem;
}

.use-cases-subtitle {
  font-size: 1.25rem;
  color: #9e9e9e;
  text-align: center;
  margin-bottom: 3rem;
}

.use-cases-tabs {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 3rem;
  position: relative;
}

.use-cases-tabs::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 0;
  width: 100%;
  height: 1px;
  background-color: #333;
}

.tab-button {
  background: transparent;
  border: none;
  color: #9e9e9e;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: color 0.3s ease;
  position: relative;
}

.tab-button:hover {
  color: #ffffff;
}

.tab-button.active {
  color: #ffffff;
}

.tab-button.active::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: var(--color-primary, #f5c518);
  z-index: 1;
}

.use-cases-content {
  display: flex;
  flex-wrap: wrap;
  gap: 3rem;
  align-items: center;
}

.content-left {
  flex: 1;
  min-width: 300px;
}

.content-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
}

.content-description {
  font-size: 1.1rem;
  line-height: 1.6;
  color: #d1d1d1;
}

.content-right {
  flex: 2;
  min-width: 300px;
}

.image-carousel {
  position: relative;
  overflow: hidden;
  border-radius: 12px;
}

.carousel-images {
  display: flex;
  transition: transform 0.5s ease;
}

.carousel-image {
  width: 100%;
  flex-shrink: 0;
  object-fit: cover;
  border-radius: 12px;
}

.carousel-controls {
  position: absolute;
  bottom: 20px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
}

.control-button {
  background-color: rgba(0, 0, 0, 0.6);
  color: #ffffff;
  border: none;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.control-button:hover {
  background-color: rgba(0, 0, 0, 0.8);
}

.control-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.carousel-dots {
  display: flex;
  gap: 0.5rem;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.4);
  border: none;
  padding: 0;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.dot.active {
  background-color: var(--color-primary, #f5c518);
  transform: scale(1.2);
}

/* Responsive adjustments */
@media (max-width: 992px) {
  .use-cases-content {
    flex-direction: column;
  }

  .content-left {
    text-align: center;
  }

  .use-cases-title {
    font-size: 2.5rem;
  }

  .content-title {
    font-size: 2rem;
  }
}

.language-switcher select {
  padding: 8px;
  border-radius: 5px;
  border: 1px solid #ccc;
  background-color: #fff;
  margin-right: 10px;
  cursor: pointer;
}

@media (max-width: 768px) {
  .use-cases-tabs {
    gap: 0.5rem;
  }

  .tab-button {
    font-size: 0.9rem;
    padding: 0.5rem;
  }

  .use-cases-title {
    font-size: 2rem;
  }
}

@media (max-width: 576px) {
  .use-cases-section {
    padding: 3rem 0;
  }

  .use-cases-tabs {
    flex-direction: column;
    gap: 0.25rem;
  }

  .tab-button {
    width: 100%;
    padding: 0.75rem;
    text-align: center;
  }

  .tab-button.active::after {
    height: 1px;
  }
}

.feature-sections {
  width: 100%;
  background-color: #000000;
  color: #ffffff;
}

.feature-section {
  padding: 5rem 2rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.feature-container {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  max-height: 500px;
  gap: 4rem;
}

.feature-section-reverse .feature-container {
  flex-direction: row-reverse;
}

.feature-image {
  flex: 1;
  min-width: 500px;
  border-radius: 16px;
  transform: scale(1,0.5);
  overflow: hidden;
}

.feature-image img {
  width: 100%;
  height: auto;
  max-height: 100px;
  display: block;
  border-radius: 16px;
  transition: transform 0.5s ease;
}

.feature-image:hover img {
  transform: scale(1.02);
}

.feature-image-colored {
  background-color: var(--feature-bg-color, #FFF176);
  padding: 2rem;
}

.feature-content {
  flex: 1;
  min-width: 300px;
}

.feature-title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
}

.feature-description {
  font-size: 1.25rem;
  line-height: 1.6;
  color: #d1d1d1;
  margin-bottom: 2rem;
}

.feature-description strong {
  color: #ffffff;
}

.feature-button {
  display: inline-block;
  background-color: transparent;
  color: #ffffff;
  border: 2px solid #ffffff;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 8px;
  text-decoration: none;
  transition: all 0.3s ease;
}

.feature-button:hover {
  background-color: #ffffff;
  color: #000000;
}

/* Responsive styles */
@media (max-width: 992px) {
  .feature-container {
    flex-direction: column;
    gap: 2rem;
  }

  .feature-section-reverse .feature-container {
    flex-direction: column;
  }

  .feature-content {
    text-align: center;
  }

  .feature-title {
    font-size: 2.5rem;
  }
}

@media (max-width: 768px) {
  .feature-section {
    padding: 3rem 1.5rem;
  }

  .feature-title {
    font-size: 2rem;
  }

  .feature-description {
    font-size: 1.1rem;
  }
}

@media (max-width: 576px) {
  .feature-section {
    padding: 2.5rem 1rem;
  }

  .feature-title {
    font-size: 1.75rem;
  }

  .feature-description {
    font-size: 1rem;
  }

  .feature-button {
    width: 100%;
    text-align: center;
  }
}
</style>