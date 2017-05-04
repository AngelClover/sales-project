var cors = true
var url = cors?"http://123.206.24.238:9000/":'http://localhost:8080/'
export const API_ROOT = (process.env.NODE_ENV === 'production') ? url : url

export const CookieDomain = (process.env.NODE_ENV === 'production') ? '' :''
//export const CookieDomain = (process.env.NODE_ENV === 'production') ? '.gtah.top' :''
