import { useState } from 'react'
import MainPage from './pages/MainPage/MainPage'
import Login from './pages/Login/Login'


function App() {
  const [count, setCount] = useState(0)

  return (
   <>
    {/* <MainPage/> */}
    <Login/>
   </>
  )
}

export default App
