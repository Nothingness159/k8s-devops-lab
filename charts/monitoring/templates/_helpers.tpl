{{- define "vmagent.name" -}}
vmagent
{{- end -}}

{{- define "vmagent.fullname" -}}
{{ include "vmagent.name" . }}
{{- end -}}
