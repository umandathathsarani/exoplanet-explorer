import { ref } from 'vue'

export const authState = ref({
  isAuthenticated: !!localStorage.getItem('token'),
  token: localStorage.getItem('token') || null
})

export const login = (token) => {
  localStorage.setItem('token', token)
  authState.value.token = token
  authState.value.isAuthenticated = true
}

export const logout = () => {
  localStorage.removeItem('token')
  authState.value.token = null
  authState.value.isAuthenticated = false
}