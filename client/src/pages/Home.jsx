import react from "@heroicons/react"
import { Link } from "react-router-dom/cjs/react-router-dom"

export default function Home(){

    function goToTestForms(){

    }


    return <>
     <h1>Home</h1>
 <Link to="/formTest">
        <button>Test forms</button>
      </Link>    </>
}