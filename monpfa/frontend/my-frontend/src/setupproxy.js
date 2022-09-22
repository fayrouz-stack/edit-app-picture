const { createProxyMiddleware } = require ('http-proxy-middleware')
module.exports = app => (
    app.use (
        createProxyMiddleware ('/endpoint',
        { target:'http://localhost:5000',
        secure : false
        
    })
    )
)