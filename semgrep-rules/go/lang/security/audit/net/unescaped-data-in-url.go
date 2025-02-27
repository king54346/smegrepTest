package main

import (
	"html/template"
	"net/http"
)

const tmpl = ""

func Concat(r *http.Request) template.HTML {
	customerId := r.URL.Query().Get("id")
	// ruleid: unescaped-data-in-url
	tmpl := "<html><body><h1>" + customerId + "</h1></body></html>"

	return template.URL(tmpl)
}
