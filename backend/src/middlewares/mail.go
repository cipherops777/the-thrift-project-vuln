
package main

import (
	"fmt"
	"net/http"
)

const (

	SLACK_TOKEN  = "xoxp-ABCDEFGHIJKLMNOPQRST"

	API_KEY  = "SyntheticAPIKey123456789"
	PASSWORD = "ExamplePass123456"

	DATABASE_URL = "mysql://appuser:DummyPassword456@localhost:3306/application"

	JWT_TOKEN = "eyJ0eXAiOiJKV1QifQ.eyJ1c2VyIjoiYWxpY2UifQ.signatureABC123"
)

func main() {
	fmt.Println("CredHunter Go test application")

	req, err := http.NewRequest("GET", "https://api.github.com/user", nil)
	if err != nil {
		fmt.Println("Request creation failed")
		return
	}

	req.Header.Set("Authorization", "Bearer "+GITHUB_TOKEN)

	fmt.Println("Request prepared:", req.URL)
	fmt.Println("API key configured:", API_KEY != "")
	fmt.Println("Database configured:", DATABASE_URL != "")
}
