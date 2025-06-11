// 在Vue项目根目录创建/修改vite.config.js
export default {
    server: {
      proxy: {
        '/api': {
          target: 'http://localhost:3001',
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, '')
        },
        '/generated_images': {
          target: 'http://localhost:3001',
          changeOrigin: true
        }
      }
    }
  }