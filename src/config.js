export const API_ROOT = (process.env.NODE_ENV === 'production')
			? 'http://localhost:8080/'
			:'http://localhost:8080/'

export const CookieDomain = (process.env.NODE_ENV === 'production')
			? '.chepi.top'
			:''
