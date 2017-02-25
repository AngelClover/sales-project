import cookie from 'react-cookie'
import { CookieDomain } from '../config.js'
let cookieConfig = {}
if(CookieDomain !== ''){
  cookieConfig = { domain: CookieDomain }
}

export function saveCookie(name,value) {
  cookie.save(name, value, cookieConfig)
}

export function getCookie(name) {
  return cookie.load(name)
}

export function removeCookie(name) {
  cookie.remove(name, cookieConfig)
}

export function signOut() {
  cookie.remove('token', cookieConfig)
}

export function isLogin() {
  return !!cookie.load('token')
}

export function getStorage(name){
    return JSON.parse(localStorage.getItem(name) || "{}")
}

export function saveStorage(name, value){
    localStorage.setItem(name, JSON.stringify(value))
}

export function removeStorage(name){
    localStorage.removeItem(name)
}

export function clearStorage(){
    localStorage.clear()
}
