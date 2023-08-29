import React, { Component, useState } from "react"
import '../App.css';

function JobList() {
    const [displayApplied, setDisplayApplied] = useState(false)

    const jobApps = [
        {
          company: "Microsoft",
          position: "Software Engineer",
          url: "www.microsoft.com/jobs",
          data_applied: "2023/7/23",
          status: "Applied",
        },
        {
          company: "Booz Allen Hamilton",
          position: "Integration Engineer",
          url: "www.boozallen.com/careers",
          date_applied: "2023/08/12",
          status: "Rejected",
        },
        {
          company: "Ubisoft",
          position: "Application Developer",
          url: "www.ubisoft.com/joinus",
          date_applied: "2023/07/18",
          status: "Applied",
        }
      ]

      const appliedSwitch = () => {
        !setDisplayApplied()
      }
    
      class App extends Component {
        constructor(props) {
          super(props);
          this.state = {
            viewCompleted: false,
            jobApps: jobApps,
          }
        }
      }


}