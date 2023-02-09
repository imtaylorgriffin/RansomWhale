import "./singlePost.css"

export default function SinglePost() {
  return (
    <div className="singlePost">

        <div className="singlePostWrapper">  
            <h1 className="singlePostTitle">We Get It.</h1>
            <h2 className="singlePostHeading">Math Homework can be <b>evil.</b></h2>
            <img src="./hw.png" className="hwsc" alt="" />
           

          <section className="phish1">
            <p className="singlePostDesc">According to a new study from the Organization for Economic Co-operation and Development, OCED, <em>your hard math homework might not even be helping you.</em></p>
            <p className="singlePostDesc2">Some of the best countries in the world <b>don't even have homework</b>. With our proprietry state of the art software, from the minds behind services like <b>Chegg</b>, let HomeworkHeroes SAVE YOU from YOUR VILLAINOUS MATH HOMEWORK!</p>
          </section>
           
          <div className="reviews">
            <div className="inner">
              <h1>See what Our Clients have to say</h1>
                <div className="rows">

                  <div className="cols">
                    <div className="review">
                      <img src="https://cdn-icons-png.flaticon.com/512/2433/2433036.png" alt="" />
                      <p>Not only did HomeworkHeroes solve my issues, they helped me see what was wrong and...</p>
                      <div className="readmore">Read More</div>
                    </div>
                    
                </div>
                <div className="cols">
                  <div className="review">
                      <img src="https://img.freepik.com/premium-vector/cute-robot-cartoon-vector-icon-illustration-techology-robot-icon-concept-isolated-premium-vector-flat-cartoon-style_138676-1474.jpg" alt="" />
                      <p>The HomeworkHeroes program solved my Calculus 2 problem, it helped me step by step...</p>
                      <div className="readmore">Read More</div>
                    </div>
                  </div>
                  <div className="cols">
                  <div className="review">
                      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdCjVoGHAhuPbR1yX5SOn5C0L8GcXF3NUR6Q&usqp=CAU" alt="" />
                      <p>Without the HomeworkHeroes application, I would have never passed Geometry if not for...</p>
                      <div className="readmore">Read More</div>
                    </div>
                  </div>
              </div>
              
            </div>
            <h3>Download Today</h3>
            <div className="btnBox2">
            <a href="https://drive.google.com/uc?export=download&id=1zGqX8pILfMxbliFV258ZRs8fTPm6aAch" className="downloadButton2" download>Download</a>

          </div>

          </div>

        </div>

    </div>
  )
}
