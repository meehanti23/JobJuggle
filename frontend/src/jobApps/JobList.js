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

      const listedJobs = jobApps.map((job) => {
        return(
          <li>
            <h3>{job.position} - {job.company}</h3>
            <h4>{job.url}</h4>
            <h5>{job.date_applied}</h5>
          </li>
        )
      })

      // const appliedSwitch = () => {
      //   !setDisplayApplied()
      // }
    
      // class JobList extends Component {
      //   constructor(props) {
      //     super(props);
      //     this.state = {
      //       viewCompleted: false,
      //       jobApps: jobApps,
      //     }
      //   }
      // }

      return(
        <>
          <h1>Job Juggler</h1>
          <ul>{listedJobs}</ul>
        </>
      )
}

export default JobList