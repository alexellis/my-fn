package function

import (
	"io/ioutil"
)

// Handle a serverless request
func Handle(req []byte) string {
	file, err := ioutil.ReadFile("/var/openfaas/secrets/key")

	if err != nil {
		return err.Error()
	}

	return "Your secret was accessed and available, thanks."

	//	return "Your secret: " + string(file)
}
