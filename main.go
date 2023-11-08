package main

import (
	"net/http"
	"strconv"
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	r.GET("/square", func(c *gin.Context) {
		numberParam := c.DefaultQuery("number", "0") // Default value is 0 if "number" is not provided
		number, err := strconv.Atoi(numberParam)
		if err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid input"})
			return
		}

		result := number * number
		c.JSON(http.StatusOK, gin.H{"your_number": number, "square": result})
	})

	r.Run(":8000") // Listen and serve on 0.0.0.0:8000
}
