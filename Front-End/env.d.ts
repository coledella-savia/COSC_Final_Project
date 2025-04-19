/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_BASEURL: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}

VUE_APP_BASEURL = "http://0.0.0.0:8000";
