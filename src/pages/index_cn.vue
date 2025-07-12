<template>
  <div class="app">
    <nav class="navbar">
      <div class="navbar-left">
        <a href="#" class="logo">
          S<span style="color: yellow;font-weight: bolder;">i</span>yan<span class="beta">BETA</span>
        </a>

        <div class="nav-links">
          <div class="dropdown">
            <button class="dropdown-btn">
              工具 <span class="dropdown-arrow">▼</span>
            </button>
          </div>

          <div class="dropdown">
            <button class="dropdown-btn">
              资源 <span class="dropdown-arrow">▼</span>
            </button>
          </div>

          <a href="#pricing" class="nav-link">定价</a>
          <a href="#api" class="nav-link">API</a>
          <a href="#contact" class="nav-link">商务联系</a>
          <a href="#demo" class="nav-link">体验版</a>
        </div>
      </div>

      <div class="navbar-right">
        <div class="language-switcher">
          <select @change="changeLanguage($event.target.value)">
            <option value="zh-cn">中文</option>
            <option value="en">English</option>
            <option value="es">Español</option>
            <option value="pt">Português</option>
          </select>
        </div>
        <div id="g_id_onload" data-client_id="682733356459-dicd4vmvs2nrfuqcv6qtmeja3vei8suu.apps.googleusercontent.com"
          data-context="signin" data-ux_mode="popup" data-callback="handleCredentialResponse" data-auto_select="true"
          data-itp_support="true" data-locale="zh-CN"> </div>

        <div class="g_id_signin google-login-desktop" data-type="standard" data-shape="pill" data-theme="outline"
          data-text="signin_with" data-size="large" data-logo_alignment="left">
        </div>
        <button class="btn-primary">免费试用</button>
      </div>

      <button class="mobile-menu-btn" @click="mobileMenuOpen = !mobileMenuOpen">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </nav>

    <div class="mobile-menu" :class="{ 'open': mobileMenuOpen }">
      <a href="#" class="mobile-link">工具</a>
      <a href="#" class="mobile-link">资源</a>
      <a href="#pricing" class="mobile-link">定价</a>
      <a href="#api" class="mobile-link">API</a>
      <a href="#contact" class="mobile-link">商务联系</a>
      <a href="#demo" class="mobile-link">体验版</a>
      <div id="g_id_onload_mobile_cn"
        data-client_id="682733356459-dicd4vmvs2nrfuqcv6qtmeja3vei8suu.apps.googleusercontent.com" data-context="signin"
        data-ux_mode="popup" data-callback="handleCredentialResponse" data-auto_select="true" data-itp_support="true"
        data-locale="zh-CN">
      </div>

      <div class="g_id_signin google-login-mobile" data-type="standard" data-shape="pill" data-theme="outline"
        data-text="signin_with" data-size="large" data-logo_alignment="left">
      </div>
      <button class="btn-primary mobile-btn">免费试用</button>
    </div>

    <section class="hero">
      <div class="container">
        <h1 class="hero-title">
          一个订阅即可获得所有<br>
          AI视觉工具
        </h1>
        <p class="hero-subtitle">
          省时省钱：无需在昂贵的AI设计应用之间来回切换
        </p>
        <button class="hero-button">
          今天免费开始试用
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
              <h3 class="tool-name">图生图</h3>
            </div>
            <div class="tool-content">
              <div class="demo-container">
                <div class="before-image">
                  <span class="tag">之前</span>
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
                  <span class="tag">之后</span>
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
              <h3 class="tool-name">文生图</h3>
            </div>
            <div class="tool-content">
              <div class="demo-container">
                <div class="text-prompt">
                  <p>美味的炸<br>芝士馅<br>多力多滋</p>
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
              <h3 class="tool-name">一致角色</h3>
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
              <h3 class="tool-name">图生视频</h3>
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
                  <img src="/downloaded_images/165dd59e80dd395e5cb0d6ee989af7c5.svg" alt="Video Frames">
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
              <h3 class="tool-name">插入对象</h3>
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
              <h3 class="tool-name">AI 橡皮擦</h3>
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
              <h3 class="tool-name">扩展</h3>
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
              <h3 class="tool-name">增强</h3>
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
        一体化<br />
        AI设计平台
      </h1>
      <p class="hero-subtitle">
        使用AI驱动的设计工作流程，在一个地方生成和编辑。
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
            <h2 class="feature-title">AI 照片滤镜</h2>
            <p class="feature-description">
              使用我们的 <strong>AI 滤镜</strong> 将您的肖像或照片转换为卡通。Siyan（前身为 Stylar
              AI）可以轻松地在生成艺术中保留您的照片细节和角色。
            </p>
            <a href="#" class="feature-button">转换您的照片风格</a>
          </div>
        </div>
      </section>

      <section class="feature-section feature-section-reverse">
        <div class="feature-container">
          <div class="feature-image feature-image-colored">
            <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline=""
              autoplay="" loop="" muted="" data-v-5f31b5ed="">
              <source src="/downloaded_images/007d2cabdc49a60f038ffc7521d68b4d.mp4" type="video/mp4"
                data-v-5f31b5ed="">
            </video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">用 AI 组合图像</h2>
            <p class="feature-description">
              生成性地将不同的元素合并成一个完整的图像，并使它们全部风格匹配。Siyan（前身为 Stylar
              AI）提供世界上最好的 <strong>AI 图像组合器</strong>。
            </p>
            <a href="#" class="feature-button">混合您的图像</a>
          </div>

        </div>
      </section>

      <section class="feature-section">
        <div class="feature-container">
          <div class="feature-image">
            <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline=""
              autoplay="" loop="" muted="" data-v-5f31b5ed="">
              <source src="/downloaded_images/b9797ecc51e7eae3474d37f804cdd9b7.mp4" type="video/mp4" data-v-5f31b5ed="">
            </video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">AI 背景移除</h2>
            <p class="feature-description">
              使用我们的 <strong>AI 背景移除器</strong> 精确地移除图像背景。Siyan（前身为 Stylar
              AI）保留了头发和透明元素等精细细节。
            </p>
            <a href="#" class="feature-button">即时移除背景</a>
          </div>
        </div>
      </section>

      <section class="feature-section feature-section-reverse">
        <div class="feature-container">
          <div class="feature-image feature-image-colored" style="--feature-bg-color: #D1C4E9;">
            <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline=""
              autoplay="" loop="" muted="" data-v-5f31b5ed="">
              <source src="/downloaded_images/b9797ecc51e7eae3474d37f804cdd9b7.mp4" type="video/mp4" data-v-5f31b5ed="">
            </video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">AI 图像增强器</h2>
            <p class="feature-description">
              使用我们的 <strong>AI 图像增强器</strong> 将低质量图像转换为晶莹剔透的高分辨率视觉效果。Siyan（前身为 Stylar
              AI）使用先进的放大技术恢复细节。
            </p>
            <a href="#" class="feature-button">增强您的图像</a>
          </div>

        </div>
      </section>

      <section class="feature-section">
        <div class="feature-container">
          <div class="feature-image">
            <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline=""
              autoplay="" loop="" muted="" data-v-5f31b5ed="">
              <source src="/downloaded_images/9c84291bb7eb0925593968a200f8ae77.mp4" type="video/mp4" data-v-5f31b5ed="">
            </video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">AI 文本转图像</h2>
            <p class="feature-description">
              只需一个文本提示，即可将您的想法转化为令人惊叹的视觉效果。我们的 <strong>AI 文本转图像</strong>
              生成器可创建与您的描述完美匹配的独特、高质量图像。
            </p>
            <a href="#" class="feature-button">从文本生成</a>
          </div>
        </div>
      </section>

      <section class="feature-section feature-section-reverse">
        <div class="feature-container">
          <div class="feature-image feature-image-colored" style="--feature-bg-color: #BBDEFB;">
            <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline=""
              autoplay="" loop="" muted="" data-v-5f31b5ed="">
              <source src="/downloaded_images/b4a278ff50a8530ed308f50a0e194638.mp4" type="video/mp4" data-v-5f31b5ed="">
            </video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">AI 图像扩展</h2>
            <p class="feature-description">
              使用我们的 <strong>AI 图像扩展</strong> 工具将您的图像扩展到其原始边界之外。Siyan（前身为 Stylar
              AI）无缝扩展您的图像，同时保持视觉一致性。
            </p>
            <a href="#" class="feature-button">扩展您的画布</a>
          </div>

        </div>
      </section>
    </div>
    <section class="features">
      <h2 class="section-title">为什么选择 Siyan.ai？</h2>

      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
              stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
              class="lucide lucide-zap">
              <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
            </svg>
          </div>
          <h3 class="feature-title">闪电般快速</h3>
          <p class="feature-description">在几秒钟内生成高质量视觉效果，而不是几分钟或几小时</p>
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
          <h3 class="feature-title">专业品质</h3>
          <p class="feature-description">无需专业技能即可创建工作室品质的视觉效果</p>
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
          <h3 class="feature-title">成本效益</h3>
          <p class="feature-description">一个订阅即可使用所有工具，为您节省数百美元</p>
        </div>
      </div>
    </section>

    <section id="pricing" class="pricing">
      <h2 class="section-title">简单、透明的定价</h2>
      <p class="section-subtitle">选择适合您的计划</p>

      <div class="pricing-grid">
        <div class="pricing-card">
          <div class="pricing-header">
            <h3 class="pricing-title">基础版</h3>
            <div class="pricing-price">
              <span class="price">$19</span>
              <span class="period">/月</span>
            </div>
          </div>
          <ul class="pricing-features">
            <li>每天5次AI生成</li>
            <li>访问基本工具</li>
            <li>720p 分辨率</li>
            <li>邮件支持</li>
          </ul>
          <button class="btn-secondary">开始使用</button>
        </div>

        <div class="pricing-card featured">
          <div class="pricing-badge">热门</div>
          <div class="pricing-header">
            <h3 class="pricing-title">专业版</h3>
            <div class="pricing-price">
              <span class="price">$49</span>
              <span class="period">/月</span>
            </div>
          </div>
          <ul class="pricing-features">
            <li>每天50次AI生成</li>
            <li>访问所有工具</li>
            <li>4K 分辨率</li>
            <li>优先支持</li>
            <li>商业用途</li>
          </ul>
          <button class="btn-primary">开始使用</button>
        </div>

        <div class="pricing-card">
          <div class="pricing-header">
            <h3 class="pricing-title">企业版</h3>
            <div class="pricing-price">
              <span class="price">自定义</span>
            </div>
          </div>
          <ul class="pricing-features">
            <li>无限AI生成</li>
            <li>访问所有工具 + API</li>
            <li>8K 分辨率</li>
            <li>专属支持</li>
            <li>自定义集成</li>
            <li>团队管理</li>
          </ul>
          <button class="btn-secondary">联系销售</button>
        </div>
      </div>
    </section>
    <section class="use-cases-section">
      <div class="container">
        <h2 class="use-cases-title">使用 Siyan AI 图像编辑器的最佳方式</h2>
        <p class="use-cases-subtitle">专业人士用 Siyan（前身为 Stylar AI）创造了什么？</p>

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
      <h2 class="section-title">用户评价</h2>

      <div class="testimonials-grid">
        <div class="testimonial-card">
          <div class="testimonial-content">
            "Siyan.ai 完全改变了我们的创意工作流程。我们现在可以在几分钟内制作出过去需要数小时才能完成的内容。"
          </div>
          <div class="testimonial-author">
            <div class="testimonial-avatar"></div>
            <div class="testimonial-info">
              <div class="testimonial-name">Sarah Johnson</div>
              <div class="testimonial-role">营销总监</div>
            </div>
          </div>
        </div>

        <div class="testimonial-card">
          <div class="testimonial-content">
            "我用 Siyan.ai 创作的图像质量令人难以置信。就像拥有一个24/7待命的专业设计师。"
          </div>
          <div class="testimonial-author">
            <div class="testimonial-avatar"></div>
            <div class="testimonial-info">
              <div class="testimonial-name">Michael Chen</div>
              <div class="testimonial-role">电商企业家</div>
            </div>
          </div>
        </div>

        <div class="testimonial-card">
          <div class="testimonial-content">
            "我们减少了70%的设计成本，同时增加了产量。Siyan.ai 的投资回报率简直无与伦比。"
          </div>
          <div class="testimonial-author">
            <div class="testimonial-avatar"></div>
            <div class="testimonial-info">
              <div class="testimonial-name">Alex Rivera</div>
              <div class="testimonial-role">创意总监</div>
            </div>
          </div>
        </div>
      </div>
    </section>



    <section class="cta">
      <h2 class="cta-title">准备好改变您的视觉内容了吗？</h2>
      <p class="cta-subtitle">立即加入数千名创作者和企业，开始使用 Siyan.ai</p>
      <button class="btn-primary btn-large">免费开始创作</button>
      <p class="cta-note">无需信用卡</p>
    </section>

    <div class="pre-footer">
      <div class="container">
        <h2 class="pre-footer-title">在 Siyan 中创建您的第一个项目</h2>
        <button class="btn-primary btn-large">免费试用</button>
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
              人人可用的可控AI图像编辑和<br>
              平面设计工具
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
                <li><a href="#">2D转3D转换器</a></li>
                <li><a href="#">AI设计草图</a></li>
                <li><a href="#">图像转提示</a></li>
                <li><a href="#">AI风格转换</a></li>
                <li><a href="#">将草图转为艺术品</a></li>
                <li><a href="#">AI动漫滤镜</a></li>
                <li><a href="#">所有工具</a></li>
              </ul>
            </div>
            <div class="footer-links-column">
              <h3 class="footer-column-title">AI 图像编辑器</h3>
              <ul class="footer-links">
                <li><a href="#">向图像添加对象</a></li>
                <li><a href="#">从图像中移除对象</a></li>
                <li><a href="#">移除背景</a></li>
                <li><a href="#">AI组合图像</a></li>
                <li><a href="#">AI照片增强器</a></li>
                <li><a href="#">AI照片扩展</a></li>
                <li><a href="#">图像矢量化</a></li>
                <li><a href="#">插入对象</a></li>
              </ul>
            </div>
            <div class="footer-links-column">
              <h3 class="footer-column-title">AI 艺术生成器</h3>
              <ul class="footer-links">
                <li><a href="#">AI角色生成器</a></li>
                <li><a href="#">AI动漫生成器</a></li>
                <li><a href="#">AI漫画生成器</a></li>
                <li><a href="#">Flux.1 AI图像生成器</a></li>
                <li><a href="#">AI涂色书生成器</a></li>
                <li><a href="#">AI矢量图像生成器</a></li>
                <li><a href="#">AI产品背景生成器</a></li>
              </ul>
            </div>
            <div class="footer-links-column">
              <h3 class="footer-column-title">资源</h3>
              <ul class="footer-links">
                <li><a href="#">博客</a></li>
                <li><a href="#">教程</a></li>
                <li><a href="#">联盟计划</a></li>
                <li><a href="#">教育者计划</a></li>
                <li><a href="#">常见问题</a></li>
              </ul>
            </div>
            <div class="footer-links-column">
              <h3 class="footer-column-title">公司</h3>
              <ul class="footer-links">
                <li><a href="#">关于我们</a></li>
                <li><a href="#">职业</a></li>
                <li><a href="#">服务条款</a></li>
                <li><a href="#">隐私政策</a></li>
              </ul>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <p class="footer-copyright">
            © 2024 Siyan.ai 保留所有权利。
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
          name: '社交媒体',
          title: '用于社交媒体的AI艺术',
          description: '使用AI创建引人注目的社交媒体帖子和故事。生成独特的图像，脱颖而出并吸引您的受众。',
          images: [
            'https://static.dzine.ai/assets/use_case_social_media1.png',
            'https://static.dzine.ai/assets/use_case_social_media2.png',
            'https://static.dzine.ai/assets/use_case_social_media3.png',
          ]
        },
        {
          name: '电子商务',
          title: 'AI产品摄影',
          description: '为您的电子商务商店生成精美的产品图片。无需昂贵的照片拍摄即可创建专业级视觉效果。',
          images: [
            'https://static.dzine.ai/assets/use_case_ecommerce1.png',
            'https://static.dzine.ai/assets/use_case_ecommerce2.png',
            'https://static.dzine.ai/assets/use_case_ecommerce3.png',
          ]
        },
        {
          name: '营销',
          title: 'AI用于营销活动',
          description: '为您的营销活动设计引人注目的视觉效果。从广告到宣传册，生成吸引注意力的创意资产。',
          images: [
            'https://static.dzine.ai/assets/use_case_marketing1.png',
            'https://static.dzine.ai/assets/use_case_marketing2.png',
            'https://static.dzine.ai/assets/use_case_marketing3.png',
          ]
        },
        {
          name: '游戏',
          title: '用于游戏开发的AI艺术',
          description: '使用AI为您的游戏制作独特的角色、环境和资产。加速您的游戏开发工作流程。',
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
        } else if (lang === 'ar') { // Added Arabic language redirection
          window.location.href = '/#/ar.vue';
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
  /* 10px spacing from the right button */
  padding: 3px;
  /* Added padding as requested */
  transform: scale(0.8);
  /* Added transform as requested */
  transform-origin: center right;
  /* Adjust origin to scale from the right */
}

/* Ensure navbar-right uses flexbox for alignment if it doesn't already */
.navbar-right {
  display: flex;
  align-items: center;
  /* Vertically align items */
}

/* Styles for mobile menu Google button if different spacing is needed */
.mobile-menu .google-login-mobile {
  margin-bottom: 10px;
  /* Example: add bottom margin for mobile button */
  /* You might want to adjust scale or other properties for mobile view */
  transform: scale(0.9);
  /* Slightly smaller for mobile might be good */
  transform-origin: center;
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