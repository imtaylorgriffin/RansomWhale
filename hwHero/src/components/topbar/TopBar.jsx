import "./topbar.css"


export default function TopBar() {
  return (
    <div className = "top">
        <div className="topLeft">
          <img
          src="logo.png"className="logo"/>
        </div>
        
        <div className="topCenter">
            <ul className="topList">
             
              <a className="link" href="/" >
              <li className="topListItem">Home</li>
              </a>
                
                <li className="topListItem">About</li>
              
            </ul>
        </div>
        <div className="topRight">
            <ul className="contact">
              <li className="contactButton">Contact Us</li>
            </ul>
        </div>


    </div>
  )
}
