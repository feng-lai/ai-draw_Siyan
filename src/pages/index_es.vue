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
              Herramientas <span class="dropdown-arrow">▼</span>
            </button>
          </div>

          <div class="dropdown">
            <button class="dropdown-btn">
              Recursos <span class="dropdown-arrow">▼</span>
            </button>
          </div>

          <a href="#pricing" class="nav-link">Precios</a>
          <a href="#api" class="nav-link">API</a>
          <a href="#contact" class="nav-link">Contactar Ventas</a>
          <a href="#demo" class="nav-link">Reservar una Demostración</a>
        </div>
      </div>

      <div class="navbar-right">
        <div class="language-switcher">
          <select @change="changeLanguage($event.target.value)">
            <option value="es">Español</option>
            <option value="en">English</option>
            <option value="zh-cn">中文</option>
            
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
             data-locale="es"> </div>

        <div class="g_id_signin google-login-desktop"
             data-type="standard"
             data-shape="pill"
             data-theme="outline"
             data-text="signin_with"
             data-size="large"
             data-logo_alignment="left">
        </div>
        <button class="btn-primary">Comenzar Gratis</button>
      </div>

      <button class="mobile-menu-btn" @click="mobileMenuOpen = !mobileMenuOpen">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </nav>

    <div class="mobile-menu" :class="{ 'open': mobileMenuOpen }">
      <a href="#" class="mobile-link">Herramientas</a>
      <a href="#" class="mobile-link">Recursos</a>
      <a href="#pricing" class="mobile-link">Precios</a>
      <a href="#api" class="mobile-link">API</a>
      <a href="#contact" class="mobile-link">Contactar Ventas</a>
      <a href="#demo" class="mobile-link">Reservar una Demostración</a>
      <div id="g_id_onload_mobile_es"
           data-client_id="682733356459-dicd4vmvs2nrfuqcv6qtmeja3vei8suu.apps.googleusercontent.com"
           data-context="signin"
           data-ux_mode="popup"
           data-callback="handleCredentialResponse"
           data-auto_select="true"
           data-itp_support="true"
           data-locale="es">
      </div>

      <div class="g_id_signin google-login-mobile"
           data-type="standard"
           data-shape="pill"
           data-theme="outline"
           data-text="signin_with"
           data-size="large"
           data-logo_alignment="left">
      </div>
      <button class="btn-primary mobile-btn">Comenzar Gratis</button>
    </div>

    <section class="hero">
      <div class="container">
        <h1 class="hero-title">
          Una Suscripción para Todas<br>
          las Herramientas Visuales de IA
        </h1>
        <p class="hero-subtitle">
          Ahorra Tiempo y Dinero: No Más Cambios Entre Aplicaciones de Diseño de IA Caras
        </p>
        <button class="hero-button">
          Comienza <strong>GRATIS</strong> hoy
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
              <h3 class="tool-name">Imagen a Imagen</h3>
            </div>
            <div class="tool-content">
              <div class="demo-container">
                <div class="before-image">
                  <span class="tag">Antes</span>
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
                  <span class="tag">Después</span>
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
              <h3 class="tool-name">Texto a Imagen</h3>
            </div>
            <div class="tool-content">
              <div class="demo-container">
                <div class="text-prompt">
                  <p>Deliciosos Doritos<br>Rellenos de Queso<br>Frito</p>
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
              <h3 class="tool-name">Personaje Consistente</h3>
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
              <h3 class="tool-name">Imagen a Video</h3>
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
              <h3 class="tool-name">Insertar Objeto</h3>
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
              <h3 class="tool-name">Borrador de IA</h3>
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
              <h3 class="tool-name">Expandir</h3>
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
              <h3 class="tool-name">Mejorar</h3>
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
        Plataforma de Diseño de IA<br />
        Todo en Uno
      </h1>
      <p class="hero-subtitle">
        Genera y edita en un solo lugar con el flujo de trabajo de diseño impulsado por IA.
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
            <h2 class="feature-title">Filtro de Fotos con IA</h2>
            <p class="feature-description">
              Transforma tu retrato o foto a caricatura con nuestro <strong>Filtro de IA</strong>. Siyan (anteriormente Stylar
              AI) facilita la conservación de los detalles de tu foto y personajes en el arte generativo.
            </p>
            <a href="#" class="feature-button">Transforma tu estilo de foto</a>
          </div>
        </div>
      </section>

      <section class="feature-section feature-section-reverse">
        <div class="feature-container">
          <div class="feature-image feature-image-colored">
            <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="/downloaded_images/007d2cabdc49a60f038ffc7521d68b4d.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">Combina Imágenes con IA</h2>
            <p class="feature-description">
              Fusiona generativamente diferentes elementos en una imagen completa, y haz que todos coincidan en estilo. Siyan
              (anteriormente Stylar AI) ofrece el mejor <strong>Combinador de Imágenes con IA</strong> del mundo.
            </p>
            <a href="#" class="feature-button">Mezcla tus imágenes</a>
          </div>

        </div>
      </section>

      <section class="feature-section">
        <div class="feature-container">
          <div class="feature-image">
            <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="/downloaded_images/b9797ecc51e7eae3474d37f804cdd9b7.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">Eliminación de Fondo con IA</h2>
            <p class="feature-description">
              Elimina fondos de tus imágenes con perfecta precisión usando nuestro <strong>Eliminador de Fondo con
                IA</strong>. Siyan (anteriormente Stylar AI) conserva detalles finos como el cabello y elementos transparentes.
            </p>
            <a href="#" class="feature-button">Elimina fondos al instante</a>
          </div>
        </div>
      </section>

      <section class="feature-section feature-section-reverse">
        <div class="feature-container">
          <div class="feature-image feature-image-colored" style="--feature-bg-color: #D1C4E9;">
            <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="/downloaded_images/b9797ecc51e7eae3474d37f804cdd9b7.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">Mejorador de Imágenes con IA</h2>
            <p class="feature-description">
              Transforma imágenes de baja calidad en visuales nítidas y de alta resolución con nuestro <strong>Mejorador de
                Imágenes con IA</strong>. Siyan (anteriormente Stylar AI) utiliza tecnología de escalado avanzada para restaurar detalles.
            </p>
            <a href="#" class="feature-button">Mejora tus imágenes</a>
          </div>

        </div>
      </section>

      <section class="feature-section">
        <div class="feature-container">
          <div class="feature-image">
            <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="/downloaded_images/9c84291bb7eb0925593968a200f8ae77.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">Texto a Imagen con IA</h2>
            <p class="feature-description">
              Convierte tus ideas en visuales impresionantes con solo una indicación de texto. Nuestro generador de
              <strong>Texto a Imagen con IA</strong> crea imágenes únicas y de alta calidad que coinciden perfectamente con tus descripciones.
            </p>
            <a href="#" class="feature-button">Genera desde texto</a>
          </div>
        </div>
      </section>

      <section class="feature-section feature-section-reverse">
        <div class="feature-container">
          <div class="feature-image feature-image-colored" style="--feature-bg-color: #BBDEFB;">
            <video class="vi" poster="/downloaded_images/d501e0ebc2c10ec9dfc39a2f3eb71d04.jpg" playsinline="" autoplay="" loop="" muted="" data-v-5f31b5ed=""><source src="/downloaded_images/b4a278ff50a8530ed308f50a0e194638.mp4" type="video/mp4" data-v-5f31b5ed=""></video>
          </div>
          <div class="feature-content">
            <h2 class="feature-title">Expansión de Imagen con IA</h2>
            <p class="feature-description">
              Expande tus imágenes más allá de sus límites originales con nuestra herramienta de <strong>Expansión de
                Imagen con IA</strong>. Siyan (anteriormente Stylar AI) extiende tus imágenes sin problemas mientras mantiene la consistencia visual.
            </p>
            <a href="#" class="feature-button">Expande tu lienzo</a>
          </div>

        </div>
      </section>
    </div>
    <section class="features">
      <h2 class="section-title">¿Por qué elegir Siyan.ai?</h2>

      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
              stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
              class="lucide lucide-zap">
              <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
            </svg>
          </div>
          <h3 class="feature-title">Velocidad Relámpago</h3>
          <p class="feature-description">Genera visuales de alta calidad en segundos, no en minutos u horas</p>
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
          <h3 class="feature-title">Calidad Profesional</h3>
          <p class="feature-description">Crea visuales con calidad de estudio sin necesidad de habilidades profesionales</p>
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
          <h3 class="feature-title">Rentable</h3>
          <p class="feature-description">Una suscripción para todas las herramientas, ahorrándote cientos de dólares</p>
        </div>
      </div>
    </section>

    <section id="pricing" class="pricing">
      <h2 class="section-title">Precios Simples y Transparentes</h2>
      <p class="section-subtitle">Elige el plan que mejor se adapte a ti</p>

      <div class="pricing-grid">
        <div class="pricing-card">
          <div class="pricing-header">
            <h3 class="pricing-title">Básico</h3>
            <div class="pricing-price">
              <span class="price">$19</span>
              <span class="period">/mes</span>
            </div>
          </div>
          <ul class="pricing-features">
            <li>5 generaciones de IA por día</li>
            <li>Acceso a herramientas básicas</li>
            <li>Resolución 720p</li>
            <li>Soporte por correo electrónico</li>
          </ul>
          <button class="btn-secondary">Comenzar</button>
        </div>

        <div class="pricing-card featured">
          <div class="pricing-badge">Popular</div>
          <div class="pricing-header">
            <h3 class="pricing-title">Pro</h3>
            <div class="pricing-price">
              <span class="price">$49</span>
              <span class="period">/mes</span>
            </div>
          </div>
          <ul class="pricing-features">
            <li>50 generaciones de IA por día</li>
            <li>Acceso a todas las herramientas</li>
            <li>Resolución 4K</li>
            <li>Soporte prioritario</li>
            <li>Uso comercial</li>
          </ul>
          <button class="btn-primary">Comenzar</button>
        </div>

        <div class="pricing-card">
          <div class="pricing-header">
            <h3 class="pricing-title">Empresa</h3>
            <div class="pricing-price">
              <span class="price">Personalizado</span>
            </div>
          </div>
          <ul class="pricing-features">
            <li>Generaciones de IA ilimitadas</li>
            <li>Acceso a todas las herramientas + API</li>
            <li>Resolución 8K</li>
            <li>Soporte dedicado</li>
            <li>Integraciones personalizadas</li>
            <li>Gestión de equipos</li>
          </ul>
          <button class="btn-secondary">Contactar Ventas</button>
        </div>
      </div>
    </section>
    <section class="use-cases-section">
      <div class="container">
        <h2 class="use-cases-title">Mejores Maneras de Usar el Editor de Imágenes de IA de Siyan</h2>
        <p class="use-cases-subtitle">¿Qué crean los profesionales con Siyan (anteriormente Stylar AI)?</p>

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
      <h2 class="section-title">Lo que Dicen Nuestros Usuarios</h2>

      <div class="testimonials-grid">
        <div class="testimonial-card">
          <div class="testimonial-content">
            "Siyan.ai ha transformado completamente nuestro flujo de trabajo creativo. Estamos produciendo contenido en minutos que solía tomar horas."
          </div>
          <div class="testimonial-author">
            <div class="testimonial-avatar"></div>
            <div class="testimonial-info">
              <div class="testimonial-name">Sarah Johnson</div>
              <div class="testimonial-role">Directora de Marketing</div>
            </div>
          </div>
        </div>

        <div class="testimonial-card">
          <div class="testimonial-content">
            "La calidad de las imágenes que puedo crear con Siyan.ai es increíble. Es como tener un diseñador profesional de guardia 24/7."
          </div>
          <div class="testimonial-author">
            <div class="testimonial-avatar"></div>
            <div class="testimonial-info">
              <div class="testimonial-name">Michael Chen</div>
              <div class="testimonial-role">Empresario de Comercio Electrónico</div>
            </div>
          </div>
        </div>

        <div class="testimonial-card">
          <div class="testimonial-content">
            "Hemos reducido nuestros costos de diseño en un 70% mientras aumentamos nuestra producción. El ROI con Siyan.ai es simplemente inigualable."
          </div>
          <div class="testimonial-author">
            <div class="testimonial-avatar"></div>
            <div class="testimonial-info">
              <div class="testimonial-name">Alex Rivera</div>
              <div class="testimonial-role">Director Creativo</div>
            </div>
          </div>
        </div>
      </div>
    </section>



    <section class="cta">
      <h2 class="cta-title">¿Listo para Transformar tu Contenido Visual?</h2>
      <p class="cta-subtitle">Únete a miles de creadores y empresas que usan Siyan.ai hoy</p>
      <button class="btn-primary btn-large">Comienza a Crear Gratis</button>
      <p class="cta-note">No se requiere tarjeta de crédito</p>
    </section>

    <div class="pre-footer">
      <div class="container">
        <h2 class="pre-footer-title">Crea tu Primer Proyecto en Siyan</h2>
        <button class="btn-primary btn-large">Comenzar Gratis</button>
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
              Edición de Imágenes con IA Controlable y<br>
              Herramienta de Diseño Gráfico para Todos
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
              <h3 class="footer-column-title">FILTRO DE FOTOS CON IA</h3>
              <ul class="footer-links">
                <li><a href="#">Convertidor 2D a 3D</a></li>
                <li><a href="#">Boceto de Diseño de IA</a></li>
                <li><a href="#">Imagen a Prompt</a></li>
                <li><a href="#">Transferencia de Estilo de IA</a></li>
                <li><a href="#">Convertir Boceto a Arte</a></li>
                <li><a href="#">Filtro de Anime con IA</a></li>
                <li><a href="#">Todas las Herramientas</a></li>
              </ul>
            </div>
            <div class="footer-links-column">
              <h3 class="footer-column-title">EDITOR DE IMÁGENES CON IA</h3>
              <ul class="footer-links">
                <li><a href="#">Añadir Objeto a Imagen</a></li>
                <li><a href="#">Eliminar Objeto de Imagen</a></li>
                <li><a href="#">Eliminar Fondo</a></li>
                <li><a href="#">Combinar Imágenes con IA</a></li>
                <li><a href="#">Mejorador de Fotos con IA</a></li>
                <li><a href="#">Expansión de Fotos con IA</a></li>
                <li><a href="#">Vectorizar Imagen</a></li>
                <li><a href="#">Insertar Objeto</a></li>
              </ul>
            </div>
            <div class="footer-links-column">
              <h3 class="footer-column-title">GENERADOR DE ARTE CON IA</h3>
              <ul class="footer-links">
                <li><a href="#">Generador de Personajes con IA</a></li>
                <li><a href="#">Generador de Anime con IA</a></li>
                <li><a href="#">Generador de Cómics con IA</a></li>
                <li><a href="#">Generador de Imágenes Flux.1 AI</a></li>
                <li><a href="#">Generador de Libros para Colorear con IA</a></li>
                <li><a href="#">Generador de Imágenes Vectoriales con IA</a></li>
                <li><a href="#">Generador de Fondos de Productos con IA</a></li>
              </ul>
            </div>
            <div class="footer-links-column">
              <h3 class="footer-column-title">RECURSOS</h3>
              <ul class="footer-links">
                <li><a href="#">Blog</a></li>
                <li><a href="#">Tutorial</a></li>
                <li><a href="#">Programa de Afiliados</a></li>
                <li><a href="#">Programa para Educadores</a></li>
                <li><a href="#">Preguntas Frecuentes</a></li>
              </ul>
            </div>
            <div class="footer-links-column">
              <h3 class="footer-column-title">Empresa</h3>
              <ul class="footer-links">
                <li><a href="#">Sobre Nosotros</a></li>
                <li><a href="#">Carreras</a></li>
                <li><a href="#">Términos de Servicio</a></li>
                <li><a href="#">Política de Privacidad</a></li>
              </ul>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <p class="footer-copyright">
            © 2024 Siyan.ai Todos los derechos reservados.
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
          name: 'Redes Sociales',
          title: 'Arte de IA para Redes Sociales',
          description: 'Crea publicaciones e historias llamativas para redes sociales con IA. Genera imágenes únicas que destaquen y enganchen a tu audiencia.',
          images: [
            'https://static.dzine.ai/assets/use_case_social_media1.png',
            'https://static.dzine.ai/assets/use_case_social_media2.png',
            'https://static.dzine.ai/assets/use_case_social_media3.png',
          ]
        },
        {
          name: 'E-commerce',
          title: 'Fotografía de Productos con IA',
          description: 'Genera imágenes de productos impresionantes para tu tienda de comercio electrónico. Crea visuales de calidad profesional sin necesidad de costosas sesiones de fotos.',
          images: [
            'https://static.dzine.ai/assets/use_case_ecommerce1.png',
            'https://static.dzine.ai/assets/use_case_ecommerce2.png',
            'https://static.dzine.ai/assets/use_case_ecommerce3.png',
          ]
        },
        {
          name: 'Marketing',
          title: 'IA para Campañas de Marketing',
          description: 'Diseña visuales convincentes para tus campañas de marketing. Desde anuncios hasta folletos, genera activos creativos que capturen la atención.',
          images: [
            'https://static.dzine.ai/assets/use_case_marketing1.png',
            'https://static.dzine.ai/assets/use_case_marketing2.png',
            'https://static.dzine.ai/assets/use_case_marketing3.png',
          ]
        },
        {
          name: 'Gaming',
          title: 'Arte de IA para Desarrollo de Juegos',
          description: 'Produce personajes, entornos y activos únicos para tus juegos con IA. Acelera tu flujo de trabajo de desarrollo de juegos.',
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
          console.log('Inicio de sesión exitoso:', data);
          // Handle successful login, e.g., redirect or update UI
        })
        .catch(error => {
          console.error('Fallo en el inicio de sesión:', error);
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
  margin-right: 10px; /* 10px spacing from the right button */
  padding: 3px; /* Added padding as requested */
  transform: scale(0.8); /* Added transform as requested */
  transform-origin: center right; /* Adjust origin to scale from the right */
}

/* Ensure navbar-right uses flexbox for alignment if it doesn't already */
.navbar-right {
  display: flex;
  align-items: center; /* Vertically align items */
}

/* Styles for mobile menu Google button if different spacing is needed */
.mobile-menu .google-login-mobile {
  margin-bottom: 10px; /* Example: add bottom margin for mobile button */
  /* You might want to adjust scale or other properties for mobile view */
  transform: scale(0.9); /* Slightly smaller for mobile might be good */
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