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
                أدوات <span class="dropdown-arrow">▼</span>
              </button>
            </div>
  
            <div class="dropdown">
              <button class="dropdown-btn">
                مصادر <span class="dropdown-arrow">▼</span>
              </button>
            </div>
  
            <a href="#pricing" class="nav-link">التسعير</a>
            <a href="#api" class="nav-link">واجهة برمجة التطبيقات</a>
            <a href="#contact" class="nav-link">الاتصال بالمبيعات</a>
            <a href="#demo" class="nav-link">حجز عرض توضيحي</a>
          </div>
        </div>
  
        <div class="navbar-right">
         
            <div class="language-switcher">
          <select @change="changeLanguage($event.target.value)">
            <option value="zh-cn">中文</option>
            <option value="en">English</option>
            <option value="es">Español</option>
            <option value="pt">Português</option>
            <option value="jp">日本語</option>
            <option value="ar">العربية</option>
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
          <button class="btn-primary">ابدأ مجانًا</button>
        </div>
  
      </nav>
  
      <div class="mobile-menu" :class="{ 'open': mobileMenuOpen }">
        <a href="#" class="mobile-link">أدوات</a>
        <a href="#" class="mobile-link">مصادر</a>
        <a href="#pricing" class="mobile-link">التسعير</a>
        <a href="#api" class="mobile-link">واجهة برمجة التطبيقات</a>
        <a href="#contact" class="mobile-link">الاتصال بالمبيعات</a>
        <a href="#demo" class="mobile-link">حجز عرض توضيحي</a>
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
        <button class="btn-primary mobile-btn">ابدأ مجانًا</button>
      </div>
  
      <section class="hero">
        <div class="container">
          <h1 class="hero-title">
            اشتراك واحد لجميع<br>
            أدوات الذكاء الاصطناعي المرئية
          </h1>
          <p class="hero-subtitle">
            وفر الوقت والمال: لا مزيد من التبديل بين تطبيقات تصميم الذكاء الاصطناعي باهظة الثمن
          </p>
          <button class="hero-button">
            ابدأ مجانًا اليوم
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
                <h3 class="tool-name">تحويل الصورة إلى صورة</h3>
              </div>
              <div class="tool-content">
                <div class="demo-container">
                  <div class="before-image">
                    <span class="tag">قبل</span>
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
                    <span class="tag">بعد</span>
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
                <h3 class="tool-name">تحويل النص إلى صورة</h3>
              </div>
              <div class="tool-content">
                <div class="demo-container">
                  <div class="text-prompt">
                    <p>دوريتوس مقلية لذيذة<br>محشوة بالجبن</p>
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
                <h3 class="tool-name">شخصية متناسقة</h3>
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
                <h3 class="tool-name">تحويل الصورة إلى فيديو</h3>
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
                <h3 class="tool-name">إدراج كائن</h3>
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
                <h3 class="tool-name">ممحاة الذكاء الاصطناعي</h3>
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
                <h3 class="tool-name">توسيع</h3>
              </div>
              <div class="tool-content">
                <div class="expand-demo">
                  <img src="/downloaded_images/67e97348fd18b7bc4c74c40ec1cf76b8.png" alt="Portrait">
                  <div class="expand-arrows">
                    <div class="arrow left">
                      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                        stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="m15 18l-6-6 6-6" />
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
                <h3 class="tool-name">تحسين</h3>
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
          منصة تصميم شاملة<br />
          بالذكاء الاصطناعي
        </h1>
        <p class="hero-subtitle">
          أنشئ وحرر في مكان واحد باستخدام سير عمل التصميم المدعوم بالذكاء الاصطناعي.
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
              <h2 class="feature-title">فلتر الصور بالذكاء الاصطناعي</h2>
              <p class="feature-description">
                حول صورتك الشخصية أو صورتك إلى رسوم متحركة باستخدام <strong>فلتر الذكاء الاصطناعي</strong> الخاص بنا. سيان (المعروف سابقًا باسم ستايلار إيه آي) يجعل من السهل الاحتفاظ بتفاصيل صورك وشخصياتك في الفن التوليدي.
              </p>
              <a href="#" class="feature-button">حول نمط صورتك</a>
            </div>
          </div>
        </section>
  
        <section class="feature-section feature-section-reverse">
          <div class="feature-container">
            <div class="feature-image feature-image-colored">
              <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="/downloaded_images/007d2cabdc49a60f038ffc7521d68b4d.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
            </div>
            <div class="feature-content">
              <h2 class="feature-title">دمج الصور بالذكاء الاصطناعي</h2>
              <p class="feature-description">
                ادمج عناصر مختلفة بشكل توليدي في صورة كاملة واحدة، واجعلها كلها متطابقة في الأسلوب. تقدم سيان (المعروف سابقًا باسم ستايلار إيه آي) أفضل <strong>دمج صور بالذكاء الاصطناعي</strong> في العالم.
              </p>
              <a href="#" class="feature-button">امزج صورك</a>
            </div>
  
          </div>
        </section>
  
        <section class="feature-section">
          <div class="feature-container">
            <div class="feature-image">
              <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="/downloaded_images/b9797ecc51e7eae3474d37f804cdd9b7.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
            </div>
            <div class="feature-content">
              <h2 class="feature-title">إزالة الخلفية بالذكاء الاصطناعي</h2>
              <p class="feature-description">
                قم بإزالة الخلفيات من صورك بدقة متناهية باستخدام أداة <strong>إزالة الخلفية بالذكاء الاصطناعي</strong>. تحافظ سيان (المعروف سابقًا باسم ستايلار إيه آي) على التفاصيل الدقيقة مثل الشعر والعناصر الشفافة.
              </p>
              <a href="#" class="feature-button">إزالة الخلفيات فورًا</a>
            </div>
          </div>
        </section>
  
        <section class="feature-section feature-section-reverse">
          <div class="feature-container">
            <div class="feature-image feature-image-colored" style="--feature-bg-color: #D1C4E9;">
              <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="/downloaded_images/b9797ecc51e7eae3474d37f804cdd9b7.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
            </div>
            <div class="feature-content">
              <h2 class="feature-title">محسن الصور بالذكاء الاصطناعي</h2>
              <p class="feature-description">
                حول الصور منخفضة الجودة إلى صور واضحة تمامًا وعالية الدقة باستخدام <strong>محسن الصور بالذكاء الاصطناعي</strong>. تستخدم سيان (المعروف سابقًا باسم ستايلار إيه آي) تقنية ترقية متقدمة لاستعادة التفاصيل.
              </p>
              <a href="#" class="feature-button">حسن صورك</a>
            </div>
  
          </div>
        </section>
  
        <section class="feature-section">
          <div class="feature-container">
            <div class="feature-image">
              <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="/downloaded_images/9c84291bb7eb0925593968a200f8ae77.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
            </div>
            <div class="feature-content">
              <h2 class="feature-title">تحويل النص إلى صورة بالذكاء الاصطناعي</h2>
              <p class="feature-description">
                حول أفكارك إلى صور بصرية مذهلة بمجرد وصف نصي. مولد <strong>النص إلى صورة بالذكاء الاصطناعي</strong> الخاص بنا ينشئ صورًا فريدة وعالية الجودة تتوافق مع أوصافك تمامًا.
              </p>
              <a href="#" class="feature-button">أنشئ من النص</a>
            </div>
          </div>
        </section>
  
        <section class="feature-section feature-section-reverse">
          <div class="feature-container">
            <div class="feature-image feature-image-colored" style="--feature-bg-color: #BBDEFB;">
              <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="/downloaded_images/b4a278ff50a8530ed308f50a0e194638.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
            </div>
            <div class="feature-content">
              <h2 class="feature-title">توسيع الصورة بالذكاء الاصطناعي</h2>
              <p class="feature-description">
                وسع صورك إلى ما بعد حدودها الأصلية باستخدام أداة <strong>توسيع الصور بالذكاء الاصطناعي</strong>. توسع سيان (المعروف سابقًا باسم ستايلار إيه آي) صورك بسلاسة مع الحفاظ على التناسق البصري.
              </p>
              <a href="#" class="feature-button">وسع مساحتك</a>
            </div>
  
          </div>
        </section>
      </div>
      <section class="features">
        <h2 class="section-title">لماذا تختار Siyan.ai؟</h2>
  
        <div class="features-grid">
          <div class="feature-card">
            <div class="feature-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                class="lucide lucide-zap">
                <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
              </svg>
            </div>
            <h3 class="feature-title">سرعة البرق</h3>
            <p class="feature-description">أنشئ مرئيات عالية الجودة في ثوانٍ، وليس دقائق أو ساعات</p>
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
            <h3 class="feature-title">جودة احترافية</h3>
            <p class="feature-description">أنشئ مرئيات بجودة استوديو بدون مهارات احترافية</p>
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
            <h3 class="feature-title">فعالة من حيث التكلفة</h3>
            <p class="feature-description">اشتراك واحد لجميع الأدوات، مما يوفر لك مئات الدولارات</p>
          </div>
        </div>
      </section>
  
      <section id="pricing" class="pricing">
        <h2 class="section-title">تسعير بسيط وشفاف</h2>
        <p class="section-subtitle">اختر الخطة التي تناسبك</p>
  
        <div class="pricing-grid">
          <div class="pricing-card">
            <div class="pricing-header">
              <h3 class="pricing-title">أساسي</h3>
              <div class="pricing-price">
                <span class="price">$19</span>
                <span class="period">/شهر</span>
              </div>
            </div>
            <ul class="pricing-features">
              <li>5 جيل بالذكاء الاصطناعي يوميًا</li>
              <li>الوصول إلى الأدوات الأساسية</li>
              <li>دقة 720 بكسل</li>
              <li>دعم البريد الإلكتروني</li>
            </ul>
            <button class="btn-secondary">ابدأ</button>
          </div>
  
          <div class="pricing-card featured">
            <div class="pricing-badge">شائع</div>
            <div class="pricing-header">
              <h3 class="pricing-title">احترافي</h3>
              <div class="pricing-price">
                <span class="price">$49</span>
                <span class="period">/شهر</span>
              </div>
            </div>
            <ul class="pricing-features">
              <li>50 جيل بالذكاء الاصطناعي يوميًا</li>
              <li>الوصول إلى جميع الأدوات</li>
              <li>دقة 4K</li>
              <li>دعم الأولوية</li>
              <li>الاستخدام التجاري</li>
            </ul>
            <button class="btn-primary">ابدأ</button>
          </div>
  
          <div class="pricing-card">
            <div class="pricing-header">
              <h3 class="pricing-title">مؤسسة</h3>
              <div class="pricing-price">
                <span class="price">مخصص</span>
              </div>
            </div>
            <ul class="pricing-features">
              <li>أجيال غير محدودة بالذكاء الاصطناعي</li>
              <li>الوصول إلى جميع الأدوات + واجهة برمجة التطبيقات</li>
              <li>دقة 8K</li>
              <li>دعم مخصص</li>
              <li>تكاملات مخصصة</li>
              <li>إدارة الفريق</li>
            </ul>
            <button class="btn-secondary">الاتصال بالمبيعات</button>
          </div>
        </div>
      </section>
      <section class="use-cases-section">
        <div class="container">
          <h2 class="use-cases-title">أفضل الطرق لاستخدام محرر صور Siyan AI</h2>
          <p class="use-cases-subtitle">ماذا ينشئ المحترفون باستخدام Siyan (المعروف سابقًا باسم Stylar AI)؟</p>
  
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
        <h2 class="section-title">ماذا يقول مستخدمونا</h2>
  
        <div class="testimonials-grid">
          <div class="testimonial-card">
            <div class="testimonial-content">
              "لقد غير Siyan.ai سير عملنا الإبداعي بالكامل. نحن ننتج محتوى في دقائق كان يستغرق ساعات."
            </div>
            <div class="testimonial-author">
              <div class="testimonial-avatar"></div>
              <div class="testimonial-info">
                <div class="testimonial-name">سارة جونسون</div>
                <div class="testimonial-role">مديرة التسويق</div>
              </div>
            </div>
          </div>
  
          <div class="testimonial-card">
            <div class="testimonial-content">
              "جودة الصور التي يمكنني إنشاؤها باستخدام Siyan.ai لا تصدق. إنه مثل وجود مصمم محترف تحت الطلب 24/7."
            </div>
            <div class="testimonial-author">
              <div class="testimonial-avatar"></div>
              <div class="testimonial-info">
                <div class="testimonial-name">مايكل تشين</div>
                <div class="testimonial-role">رائد أعمال التجارة الإلكترونية</div>
              </div>
            </div>
          </div>
  
          <div class="testimonial-card">
            <div class="testimonial-content">
              "لقد خفضنا تكاليف التصميم بنسبة 70% مع زيادة إنتاجنا. العائد على الاستثمار مع Siyan.ai لا مثيل له ببساطة."
            </div>
            <div class="testimonial-author">
              <div class="testimonial-avatar"></div>
              <div class="testimonial-info">
                <div class="testimonial-name">أليكس ريفيرا</div>
                <div class="testimonial-role">المدير الإبداعي</div>
              </div>
            </div>
          </div>
        </div>
      </section>
  
  
  
      <section class="cta">
        <h2 class="cta-title">هل أنت مستعد لتحويل محتواك المرئي؟</h2>
        <p class="cta-subtitle">انضم إلى الآلاف من المبدعين والشركات الذين يستخدمون Siyan.ai اليوم</p>
        <button class="btn-primary btn-large">ابدأ الإنشاء مجانًا</button>
        <p class="cta-note">لا يلزم وجود بطاقة ائتمان</p>
      </section>
  
      <div class="pre-footer">
        <div class="container">
          <h2 class="pre-footer-title">أنشئ مشروعك الأول في Siyan</h2>
          <button class="btn-primary btn-large">ابدأ مجانًا</button>
        </div>
      </div>
  
      <footer class="new-footer">
        <div class="container">
          <div class="footer-top">
            <div class="footer-brand">
              <a href="#" class="footer-logo">
                <span class="logo-text">Si<span style="color: yellow;font-weight: bolder;">y</span>an</span>
                <span class="logo-beta">BETA</span>
              </a>
              <p class="footer-tagline">
                أداة تحرير صور وتصميم جرافيك بالذكاء الاصطناعي قابلة للتحكم<br>
                للجميع
              </p>
              <div class="footer-social">
                <a href="#" class="social-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                    stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z">
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
                    <path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z">
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
                <h3 class="footer-column-title">فلتر الصور بالذكاء الاصطناعي</h3>
                <ul class="footer-links">
                  <li><a href="#">محول ثنائي الأبعاد إلى ثلاثي الأبعاد</a></li>
                  <li><a href="#">رسم تصميم بالذكاء الاصطناعي</a></li>
                  <li><a href="#">تحويل الصورة إلى موجه</a></li>
                  <li><a href="#">نقل الأسلوب بالذكاء الاصطناعي</a></li>
                  <li><a href="#">تحويل الرسم إلى فن</a></li>
                  <li><a href="#">فلتر أنمي بالذكاء الاصطناعي</a></li>
                  <li><a href="#">جميع الأدوات</a></li>
                </ul>
              </div>
              <div class="footer-links-column">
                <h3 class="footer-column-title">محرر الصور بالذكاء الاصطناعي</h3>
                <ul class="footer-links">
                  <li><a href="#">إضافة كائن إلى الصورة</a></li>
                  <li><a href="#">إزالة كائن من الصورة</a></li>
                  <li><a href="#">إزالة الخلفية</a></li>
                  <li><a href="#">دمج الصور بالذكاء الاصطناعي</a></li>
                  <li><a href="#">محسن الصور بالذكاء الاصطناعي</a></li>
                  <li><a href="#">توسيع الصورة بالذكاء الاصطناعي</a></li>
                  <li><a href="#">تحويل الصورة إلى متجه</a></li>
                  <li><a href="#">إدراج كائن</a></li>
                </ul>
              </div>
              <div class="footer-links-column">
                <h3 class="footer-column-title">مولد الفن بالذكاء الاصطناعي</h3>
                <ul class="footer-links">
                  <li><a href="#">مولد الشخصيات بالذكاء الاصطناعي</a></li>
                  <li><a href="#">مولد الأنمي بالذكاء الاصطناعي</a></li>
                  <li><a href="#">مولد القصص المصورة بالذكاء الاصطناعي</a></li>
                  <li><a href="#">مولد صور Flux.1 AI</a></li>
                  <li><a href="#">مولد كتب التلوين بالذكاء الاصطناعي</a></li>
                  <li><a href="#">مولد صور المتجهات بالذكاء الاصطناعي</a></li>
                  <li><a href="#">مولد خلفيات المنتجات بالذكاء الاصكناعي</a></li>
                </ul>
              </div>
              <div class="footer-links-column">
                <h3 class="footer-column-title">المصادر</h3>
                <ul class="footer-links">
                  <li><a href="#">المدونة</a></li>
                  <li><a href="#">البرنامج التعليمي</a></li>
                  <li><a href="#">برنامج الشراكة</a></li>
                  <li><a href="#">برنامج المعلمين</a></li>
                  <li><a href="#">الأسئلة الشائعة</a></li>
                </ul>
              </div>
              <div class="footer-links-column">
                <h3 class="footer-column-title">الشركة</h3>
                <ul class="footer-links">
                  <li><a href="#">حولنا</a></li>
                  <li><a href="#">الوظائف</a></li>
                  <li><a href="#">شروط الخدمة</a></li>
                  <li><a href="#">سياسة الخصوصية</a></li>
                </ul>
              </div>
            </div>
          </div>
          <div class="footer-bottom">
            <p class="footer-copyright">
              © 2024 Siyan.ai جميع الحقوق محفوظة.
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
            name: 'وسائل التواصل الاجتماعي',
            title: 'فن الذكاء الاصطناعي لوسائل التواصل الاجتماعي',
            description: 'أنشئ منشورات وقصصًا جذابة لوسائل التواصل الاجتماعي باستخدام الذكاء الاصطناعي. أنشئ صورًا فريدة تبرز وتجذب جمهورك.',
            images: [
              'https://static.dzine.ai/assets/use_case_social_media1.png',
              'https://static.dzine.ai/assets/use_case_social_media2.png',
              'https://static.dzine.ai/assets/use_case_social_media3.png',
            ]
          },
          {
            name: 'تصميم المنتج',
            title: 'تصميم المنتجات بالذكاء الاصطناعي',
            description: 'صمم نماذج أولية للمنتجات بسرعة وأنشئ صورًا واقعية. استخدم الذكاء الاصطناعي لتصور أفكارك وابتكار تصاميم مذهلة.',
            images: [
              'https://static.dzine.ai/assets/use_case_product_design1.png',
              'https://static.dzine.ai/assets/use_case_product_design2.png',
              'https://static.dzine.ai/assets/use_case_product_design3.png',
            ]
          },
          {
            name: 'التجارة الإلكترونية',
            title: 'صور التجارة الإلكترونية بالذكاء الاصطناعي',
            description: 'أنشئ صور منتجات عالية الجودة لتحسين متجرك عبر الإنترنت. اجذب المزيد من العملاء بصور احترافية ومذهلة بصريًا.',
            images: [
              'https://static.dzine.ai/assets/use_case_ecommerce1.png',
              'https://static.dzine.ai/assets/use_case_ecommerce2.png',
              'https://static.dzine.ai/assets/use_case_ecommerce3.png',
            ]
          },
          {
            name: 'التسويق',
            title: 'مرئيات التسويق بالذكاء الاصطناعي',
            description: 'صمم حملات تسويقية مؤثرة بصور فريدة. اجذب جمهورك المستهدف وزد من تفاعل علامتك التجارية باستخدام الذكاء الاصطناعي.',
            images: [
              'https://static.dzine.ai/assets/use_case_marketing1.png',
              'https://static.dzine.ai/assets/use_case_marketing2.png',
              'https://static.dzine.ai/assets/use_case_marketing3.png',
            ]
          },
          {
            name: 'الإعلان',
            title: 'إعلانات الذكاء الاصطناعي',
            description: 'صمم إعلانات جذابة بصريًا تبرز. أنشئ محتوى إعلانيًا فريدًا يزيد من التحويلات ويزيد الوعي بالعلامة التجارية.',
            images: [
              'https://static.dzine.ai/assets/use_case_advertising1.png',
              'https://static.dzine.ai/assets/use_case_advertising2.png',
              'https://static.dzine.ai/assets/use_case_advertising3.png',
            ]
          },
          {
            name: 'التصوير الفوتوغرافي',
            title: 'التصوير الفوتوغرافي المعزز بالذكاء الاصطناعي',
            description: 'حسن صورك باستخدام أدوات التحرير المدعومة بالذكاء الاصطناعي. اجعل صورك تبدو احترافية وجميلة بشكل لا يصدق.',
            images: [
              'https://static.dzine.ai/assets/use_case_photography1.png',
              'https://static.dzine.ai/assets/use_case_photography2.png',
              'https://static.dzine.ai/assets/use_case_photography3.png',
            ]
          },
          {
            name: 'التصميم الجرافيكي',
            title: 'تصميم الجرافيك بالذكاء الاصطناعي',
            description: 'أنشئ تصاميم جرافيك مذهلة بسهولة. استخدم الذكاء الاصطناعي لتبسيط سير عمل التصميم الخاص بك وإنتاج عمل فني عالي الجودة.',
            images: [
              'https://static.dzine.ai/assets/use_case_graphic_design1.png',
              'https://static.dzine.ai/assets/use_case_graphic_design2.png',
              'https://static.dzine.ai/assets/use_case_graphic_design3.png',
            ]
          },
          {
            name: 'الرسم التوضيحي',
            title: 'رسوم توضيحية بالذكاء الاصطناعي',
            description: 'أنشئ رسومًا توضيحية فريدة ومبتكرة باستخدام الذكاء الاصطناعي. حول أفكارك إلى صور بصرية مذهلة بسهولة.',
            images: [
              'https://static.dzine.ai/assets/use_case_illustration1.png',
              'https://static.dzine.ai/assets/use_case_illustration2.png',
              'https://static.dzine.ai/assets/use_case_illustration3.png',
            ]
          },
          {
            name: 'تصميم الويب',
            title: 'تصميم الويب بالذكاء الاصطناعي',
            description: 'أنشئ أصول ويب جذابة بصريًا وتحسينات للتصميم. استخدم الذكاء الاصطناعي لإنشاء رسومات مذهلة لمواقع الويب الخاصة بك.',
            images: [
              'https://static.dzine.ai/assets/use_case_web_design1.png',
              'https://static.dzine.ai/assets/use_case_web_design2.png',
              'https://static.dzine.ai/assets/use_case_web_design3.png',
            ]
          }
        ],
      };
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
        } else if (lang === 'jp') { // Added Arabic language redirection
          window.location.href = '/#/jp.vue';
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
  /* Base styles */
  :root {
    --primary-color: #6a0dad;
    --secondary-color: #8a2be2;
    --text-color: #333;
    --bg-color: #f4f4f9;
    --card-bg: #fff;
    --border-color: #ddd;
  }
  
  body {
    font-family: 'Inter', sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    background-color: var(--bg-color);
    color: var(--text-color);
    line-height: 1.6;
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
  }
  
  h1,
  h2,
  h3 {
    margin-top: 0;
    line-height: 1.2;
  }
  
  a {
    text-decoration: none;
    color: var(--primary-color);
  }
  
  img {
    max-width: 100%;
    height: auto;
    display: block;
  }
  
  /* Navbar */
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background-color: var(--card-bg);
    border-bottom: 1px solid var(--border-color);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  }
  
  .navbar-left {
    display: flex;
    align-items: center;
  }
  
  .logo {
    font-size: 1.8rem;
    font-weight: 800;
    color: var(--primary-color);
    margin-right: 2rem;
  }
  
  .logo .beta {
    font-size: 0.8rem;
    vertical-align: super;
    color: #ffc107;
    /* Yellow color for BETA */
    margin-left: 0.2rem;
    font-weight: 600;
  }
  
  .nav-links {
    display: flex;
    align-items: center;
  }
  
  .nav-link {
    margin: 0 1rem;
    color: var(--text-color);
    font-weight: 500;
    transition: color 0.3s ease;
  }
  
  .nav-link:hover {
    color: var(--primary-color);
  }
  
  .dropdown {
    position: relative;
    display: inline-block;
  }
  
  .dropdown-btn {
    background-color: transparent;
    border: none;
    font-size: 1rem;
    font-weight: 500;
    color: var(--text-color);
    padding: 0.5rem 1rem;
    cursor: pointer;
    display: flex;
    align-items: center;
  }
  
  .dropdown-arrow {
    margin-left: 0.5rem;
    font-size: 0.8rem;
  }
  
  .dropdown-content {
    display: none;
    position: absolute;
    background-color: var(--card-bg);
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
    z-index: 1;
    border-radius: 8px;
    overflow: hidden;
  }
  
  .dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
  }
  
  .dropdown-content a:hover {
    background-color: #f1f1f1;
  }
  
  .dropdown:hover .dropdown-content {
    display: block;
  }
  
  .navbar-right {
    display: flex;
    align-items: center;
  }
  
  .language-switcher select {
    padding: 0.5rem 1rem;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    background-color: var(--card-bg);
    margin-right: 1rem;
    cursor: pointer;
  }
  
  .btn-primary {
    background-color: var(--primary-color);
    color: white;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .btn-primary:hover {
    background-color: var(--secondary-color);
  }
  
  /* Mobile Menu */
  .mobile-menu {
    display: none;
    flex-direction: column;
    background-color: var(--card-bg);
    position: absolute;
    top: 0;
    right: -100%;
    width: 70%;
    height: 100vh;
    padding: 2rem;
    box-shadow: -2px 0 5px rgba(0, 0, 0, 0.1);
    transition: right 0.3s ease;
    z-index: 1000;
  }
  
  .mobile-menu.open {
    right: 0;
  }
  
  .mobile-link {
    color: var(--text-color);
    padding: 1rem 0;
    border-bottom: 1px solid var(--border-color);
    width: 100%;
  }
  
  .mobile-btn {
    margin-top: 1.5rem;
    width: 100%;
  }
  
  /* Hero Section */
  .hero {
    background: linear-gradient(135deg, #6a0dad, #8a2be2);
    color: white;
    text-align: center;
    padding: 4rem 1rem;
    margin-bottom: 3rem;
  }
  
  .hero-title {
    font-size: 3.5rem;
    font-weight: 800;
    margin-bottom: 1.5rem;
    line-height: 1.2;
  }
  
  .hero-subtitle {
    font-size: 1.5rem;
    margin-bottom: 2.5rem;
    opacity: 0.9;
  }
  
  .hero-button {
    background-color: #ffc107;
    color: var(--primary-color);
    padding: 1rem 2rem;
    border: none;
    border-radius: 8px;
    font-size: 1.2rem;
    font-weight: 700;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .hero-button:hover {
    background-color: #ffda6a;
  }
  
  /* Tools Grid */
  .tools-grid .container {
    padding-bottom: 4rem;
  }
  
  .tools-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
  }
  
  .tool-card {
    background-color: var(--card-bg);
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 1.5rem;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  
  .tool-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
  }
  
  .tool-header {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1rem;
  }
  
  .tool-icon {
    background-color: var(--primary-color);
    color: white;
    border-radius: 50%;
    padding: 0.75rem;
    display: inline-flex;
    margin-right: 0.75rem;
  }
  
  .tool-icon svg {
    width: 24px;
    height: 24px;
  }
  
  .tool-name {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--primary-color);
  }
  
  .tool-content {
    margin-top: 1rem;
  }
  
  .demo-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
  }
  
  .before-image,
  .after-image {
    position: relative;
    flex: 1;
  }
  
  .before-image img,
  .after-image img,
  .generated-image img,
  .character-grid img,
  .video-preview img,
  .eraser-demo img,
  .expand-demo img,
  .enhance-demo img {
    border-radius: 8px;
    width: 100%;
    height: auto;
  }
  
  .tag {
    position: absolute;
    top: 0.5rem;
    left: 0.5rem;
    background-color: rgba(0, 0, 0, 0.6);
    color: white;
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-size: 0.8rem;
  }
  
  .transform-arrow {
    color: var(--primary-color);
  }
  
  .text-prompt {
    flex: 1;
    background-color: #f0f0f0;
    padding: 1rem;
    border-radius: 8px;
    min-height: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-style: italic;
    color: #555;
    font-size: 1rem;
  }
  
  .character-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.5rem;
  }
  
  .video-demo {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  
  .video-preview {
    position: relative;
    width: 100%;
    padding-top: 56.25%;
    /* 16:9 Aspect Ratio */
    background-color: black;
    border-radius: 8px;
    overflow: hidden;
  }
  
  .video-preview img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .play-button {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 1;
    cursor: pointer;
  }
  
  .video-frames {
    display: flex;
    gap: 0.5rem;
    justify-content: center;
  }
  
  .video-frames img {
    width: 30%;
    border-radius: 4px;
  }
  
  .eraser-demo {
    position: relative;
  }
  
  .eraser-circle {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 80px;
    height: 80px;
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
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 1rem;
    box-sizing: border-box;
  }
  
  .arrow {
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 50%;
    padding: 0.5rem;
    color: white;
  }
  
  .corner {
    position: absolute;
    width: 20px;
    height: 20px;
    border: 2px dashed white;
  }
  
  .top-left {
    top: 10px;
    left: 10px;
    border-right: none;
    border-bottom: none;
  }
  
  .top-right {
    top: 10px;
    right: 10px;
    border-left: none;
    border-bottom: none;
  }
  
  .bottom-left {
    bottom: 10px;
    left: 10px;
    border-right: none;
    border-top: none;
  }
  
  .bottom-right {
    bottom: 10px;
    right: 10px;
    border-left: none;
    border-top: none;
  }
  
  .enhance-demo {
    position: relative;
    width: 100%;
    height: 200px;
    overflow: hidden;
  }
  
  .split-image {
    position: relative;
    width: 200%;
    height: 100%;
    display: flex;
    transition: transform 2s ease-in-out;
  }
  
  .enhance-demo:hover .split-image {
    transform: translateX(-50%);
  }
  
  .split-image img {
    width: 50%;
    height: 100%;
    object-fit: cover;
    border-radius: 8px;
  }
  
  .split-line {
    position: absolute;
    left: 50%;
    top: 0;
    height: 100%;
    width: 2px;
    background-color: white;
    z-index: 1;
  }
  
  /* Feature Sections */
  .feature-sections {
    background-color: white;
    padding: 4rem 0;
  }
  
  .feature-section {
    padding: 3rem 0;
    border-bottom: 1px solid #eee;
  }
  
  .feature-section:last-child {
    border-bottom: none;
  }
  
  .feature-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 3rem;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
  }
  
  .feature-section-reverse .feature-container {
    flex-direction: row-reverse;
  }
  
  .feature-image {
    flex: 1;
    min-width: 400px;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    background-color: #f0f0f0;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
  }
  
  .feature-image video {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .feature-image-colored {
    background-color: var(--feature-bg-color, #E8F5E9);
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
    }
  
    .feature-section-reverse .feature-container {
      flex-direction: column;
    }
  }
  
  .features {
    padding: 4rem 1rem;
    text-align: center;
    background-color: var(--bg-color);
  }
  
  .section-title {
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 1rem;
    color: var(--primary-color);
  }
  
  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
  }
  
  .feature-card {
    background-color: var(--card-bg);
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    padding: 2rem;
    text-align: left;
  }
  
  .feature-card .feature-icon {
    background-color: var(--secondary-color);
    color: white;
    border-radius: 50%;
    padding: 0.75rem;
    display: inline-flex;
    margin-bottom: 1.5rem;
  }
  
  .feature-card .feature-title {
    font-size: 1.75rem;
    font-weight: 700;
    color: var(--text-color);
    margin-bottom: 0.75rem;
  }
  
  .feature-card .feature-description {
    font-size: 1.1rem;
    color: #555;
    line-height: 1.6;
  }
  
  /* Pricing Section */
  .pricing {
    padding: 4rem 1rem;
    text-align: center;
    background-color: white;
  }
  
  .section-subtitle {
    font-size: 1.25rem;
    color: #666;
    margin-bottom: 3rem;
  }
  
  .pricing-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
  }
  
  .pricing-card {
    background-color: var(--card-bg);
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    padding: 2.5rem;
    text-align: center;
    border: 2px solid var(--border-color);
    position: relative;
    display: flex;
    flex-direction: column;
  }
  
  .pricing-card.featured {
    border-color: var(--primary-color);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
  }
  
  .pricing-badge {
    position: absolute;
    top: 0;
    right: 0;
    background-color: var(--primary-color);
    color: white;
    padding: 0.5rem 1rem;
    border-bottom-left-radius: 12px;
    font-weight: 600;
  }
  
  .pricing-header {
    margin-bottom: 2rem;
  }
  
  .pricing-title {
    font-size: 2rem;
    font-weight: 700;
    color: var(--primary-color);
    margin-bottom: 1rem;
  }
  
  .pricing-price .price {
    font-size: 3rem;
    font-weight: 800;
    color: var(--text-color);
  }
  
  .pricing-price .period {
    font-size: 1.25rem;
    color: #666;
  }
  
  .pricing-features {
    list-style: none;
    padding: 0;
    margin: 0 0 2rem 0;
    flex-grow: 1;
  }
  
  .pricing-features li {
    margin-bottom: 0.75rem;
    font-size: 1.1rem;
    color: #555;
  }
  
  .btn-secondary {
    background-color: transparent;
    color: var(--primary-color);
    padding: 0.75rem 1.5rem;
    border: 2px solid var(--primary-color);
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  .btn-secondary:hover {
    background-color: var(--primary-color);
    color: white;
  }
  
  /* Use Cases Section */
  .use-cases-section {
    padding: 4rem 1rem;
    background-color: var(--bg-color);
  }
  
  .use-cases-title {
    font-size: 2.5rem;
    font-weight: 800;
    text-align: center;
    margin-bottom: 1rem;
    color: var(--primary-color);
  }
  
  .use-cases-subtitle {
    font-size: 1.25rem;
    color: #666;
    text-align: center;
    margin-bottom: 3rem;
  }
  
  .use-cases-tabs {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 2rem;
  }
  
  .tab-button {
    background-color: #e0e0e0;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 20px;
    cursor: pointer;
    font-size: 1rem;
    font-weight: 600;
    transition: background-color 0.3s ease, color 0.3s ease;
  }
  
  .tab-button.active {
    background-color: var(--primary-color);
    color: white;
  }
  
  .tab-button:hover:not(.active) {
    background-color: #d0d0d0;
  }
  
  .use-cases-content {
    display: flex;
    flex-direction: row;
    gap: 2rem;
    background-color: var(--card-bg);
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    padding: 2rem;
  }
  
  .content-left {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  
  .content-title {
    font-size: 2rem;
    font-weight: 700;
    color: var(--primary-color);
    margin-bottom: 1rem;
  }
  
  .content-description {
    font-size: 1.1rem;
    color: #555;
    line-height: 1.6;
  }
  
  .content-right {
    flex: 1;
  }
  
  .image-carousel {
    position: relative;
    width: 100%;
    overflow: hidden;
    border-radius: 8px;
  }
  
  .carousel-images {
    display: flex;
    transition: transform 0.5s ease-in-out;
  }
  
  .carousel-image {
    min-width: 100%;
    display: block;
  }
  
  .carousel-controls {
    position: absolute;
    bottom: 1rem;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background-color: rgba(0, 0, 0, 0.5);
    padding: 0.5rem 1rem;
    border-radius: 20px;
  }
  
  .control-button {
    background-color: transparent;
    border: none;
    color: white;
    font-size: 1.5rem;
    cursor: pointer;
    padding: 0.5rem;
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
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 50%;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .dot.active {
    background-color: white;
  }
  
  /* Testimonials Section */
  .testimonials {
    padding: 4rem 1rem;
    text-align: center;
    background-color: white;
  }
  
  .testimonials-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
  }
  
  .testimonial-card {
    background-color: var(--bg-color);
    border-radius: 12px;
    padding: 2rem;
    text-align: left;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
  }
  
  .testimonial-content {
    font-size: 1.1rem;
    line-height: 1.7;
    color: #333;
    margin-bottom: 1.5rem;
    font-style: italic;
  }
  
  .testimonial-author {
    display: flex;
    align-items: center;
  }
  
  .testimonial-avatar {
    width: 50px;
    height: 50px;
    background-color: #ccc;
    border-radius: 50%;
    margin-right: 1rem;
  }
  
  .testimonial-name {
    font-weight: 700;
    color: var(--primary-color);
  }
  
  .testimonial-role {
    font-size: 0.9rem;
    color: #666;
  }
  
  /* CTA Section */
  .cta {
    background: linear-gradient(135deg, #8a2be2, #6a0dad);
    color: white;
    text-align: center;
    padding: 4rem 1rem;
    margin-top: 3rem;
  }
  
  .cta-title {
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 1rem;
  }
  
  .cta-subtitle {
    font-size: 1.25rem;
    margin-bottom: 2rem;
    opacity: 0.9;
  }
  
  .btn-large {
    padding: 1rem 2.5rem;
    font-size: 1.2rem;
  }
  
  .cta-note {
    margin-top: 1rem;
    font-size: 0.9rem;
    opacity: 0.8;
  }
  
  /* Pre-footer */
  .pre-footer {
    background-color: #f0f0f0;
    padding: 3rem 1rem;
    text-align: center;
  }
  
  .pre-footer-title {
    font-size: 2rem;
    font-weight: 700;
    color: var(--primary-color);
    margin-bottom: 2rem;
  }
  
  /* Footer */
  .new-footer {
    background-color: #333;
    color: white;
    padding: 3rem 1rem;
  }
  
  .footer-top {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 2rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid #555;
  }
  
  .footer-brand {
    flex: 2;
    min-width: 250px;
  }
  
  .footer-logo {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
  }
  
  .logo-text {
    font-size: 2rem;
    font-weight: 800;
    color: white;
  }
  
  .logo-beta {
    font-size: 0.8rem;
    vertical-align: super;
    color: #ffc107;
    margin-left: 0.2rem;
    font-weight: 600;
  }
  
  .footer-tagline {
    font-size: 1.1rem;
    line-height: 1.6;
    color: #bbb;
  }
  
  .footer-social {
    display: flex;
    gap: 1rem;
    margin-top: 1.5rem;
  }
  
  .social-icon {
    color: white;
    transition: color 0.3s ease;
  }
  
  .social-icon:hover {
    color: var(--primary-color);
  }
  
  .footer-links-section {
    flex: 3;
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;
    justify-content: space-between;
  }
  
  .footer-links-column {
    min-width: 150px;
  }
  
  .footer-column-title {
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: white;
    text-transform: uppercase;
  }
  
  .footer-links {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .footer-links li {
    margin-bottom: 0.75rem;
  }
  
  .footer-links a {
    color: #bbb;
    font-size: 0.95rem;
    transition: color 0.3s ease;
  }
  
  .footer-links a:hover {
    color: var(--primary-color);
  }
  
  .footer-bottom {
    text-align: center;
    padding-top: 1.5rem;
  }
  
  .footer-copyright {
    font-size: 0.9rem;
    color: #bbb;
  }
  
  /* General Responsive Adjustments */
  @media (max-width: 768px) {
    .navbar .nav-links,
    .navbar .navbar-right .btn-primary,
    .navbar .navbar-right .google-login-desktop {
      display: none;
    }
  
    .navbar {
      padding: 1rem;
    }
  
    .mobile-menu {
      display: flex;
    }
  
    .hero-title {
      font-size: 2.5rem;
    }
  
    .hero-subtitle {
      font-size: 1.2rem;
    }
  
    .tools-container {
      grid-template-columns: 1fr;
    }
  
    .demo-container {
      flex-direction: column;
    }
  
    .use-cases-content {
      flex-direction: column;
    }
  
    .content-title {
      text-align: center;
    }
  
    .content-description {
      text-align: center;
    }
  
    .pricing-grid {
      grid-template-columns: 1fr;
    }
  
    .features-grid {
      grid-template-columns: 1fr;
    }
  
    .footer-top {
      flex-direction: column;
      align-items: center;
      text-align: center;
    }
  
    .footer-links-section {
      width: 100%;
      justify-content: center;
    }
  
    .footer-links-column {
      text-align: center;
      margin-bottom: 1.5rem;
    }
  }
  
  </style>
  