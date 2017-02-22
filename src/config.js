export const API_ROOT = (process.env.NODE_ENV === 'production')
			? 'http://123.206.24.238:8080'
			:'http://123.206.24.238:8080/'

export const CookieDomain = (process.env.NODE_ENV === 'production')
			? '.gtah.top'
			:''
