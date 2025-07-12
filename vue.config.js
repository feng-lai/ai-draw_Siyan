
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})
module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: './',
  devServer: {
    open: true,
    proxy: {
      '/rtsi': {
        target: 'https://www.tarikvon.cn:8005/',
        changeOrigin: true,
        pathRewrite: {
        //   '^/rtsi': ''
        }
      }
    }
  },
  css: {
    loaderOptions: {
      postcss: {
        postcssOptions: {
            plugins: [
            require('postcss-pxtorem')({
              rootValue: 16, // 换算的基数
              minPixelValue: 2,
              selectorBlackList: [], // 忽略转换正则匹配项 列入一些ui库, ['.el'] 就是忽略elementUI库
              propList: ['*'],
              mediaQuery: true,
            }),
          ]
        }
      }
    }
  }
})
