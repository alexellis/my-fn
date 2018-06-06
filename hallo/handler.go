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

	return string(file)
	// return fmt.Sprintf("When 900 years old you reach, look as good you will not. %s (Yoda)", string(req))
}
