import React, { Component, useState, useEffect } from "react"
import axios from 'axios';
import '../App.css';

function JobList() {
    const [displayApplied, setDisplayApplied] = useState(false)
    const [jobApps, setJobApps] = useState([])

      const fetchJobList = async () => {
          const response = await axios.get('/api/jobApps')
          console.log(response)
      }

      const listedJobs = jobApps.map((job) => {
        return(
          <li>
            <h3>{job.position} - {job.company}</h3>
            <h4>{job.url}</h4>
            <h5>{job.date_applied}</h5>
          </li>
        )
      })

      useEffect(() => {
        fetchJobList();
      }, [])

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