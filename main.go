package main // 测试

import (
	"github.com/gin-gonic/gin"
)

func main() {
	// 创建默认的 Gin 路由器
	r := gin.Default()

	// 定义一个 GET 路由
	r.GET("/", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "Hello, Gin!",
		})
	})

	// 定义一个带参数的路由
	r.GET("/hello/:name", func(c *gin.Context) {
		name := c.Param("name")
		c.JSON(200, gin.H{
			"message": "Hello, " + name + "!",
		})
	})

	// 启动服务器，监听 8080 端口
	r.Run(":8081") // 默认是 0.0.0.0:8080
}
