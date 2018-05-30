package function

import (
	"fmt"
)

// Handle a serverless request
func Handle(req []byte) string {
	return fmt.Sprintf("When 900 years old you reach, look as good you will not. %s (Yoda)", string(req))
}
