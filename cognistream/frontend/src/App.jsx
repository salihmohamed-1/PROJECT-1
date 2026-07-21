import { useEffect, useState } from "react";

function App() {
  const lastUpdated = new Date().toLocaleString();

  const [data, setData] = useState({
    total_commits: 0,
    pull_requests: 0,
    slack_messages: 0,
    ide_activity: 0,
  });

  useEffect(() => {
    fetch("http://127.0.0.1:8000/dashboard")
      .then((response) => response.json())
      .then((result) => setData(result))
      .catch((error) => console.error(error));
  }, []);

  return (
    <div
      style={{
        padding: "40px",
        fontFamily: "Arial, sans-serif",
        backgroundColor: "#f4f7fb",
        minHeight: "100vh",
      }}
    >
      <h1>🚀 CogniStream Dashboard</h1>

      <p>Developer Productivity Analytics Platform</p>

      <hr />

      <h2>Today's Metrics</h2>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(2, 250px)",
          gap: "20px",
          marginTop: "20px",
        }}
      >
        <div
          style={{
            padding: "20px",
            background: "#ffffff",
            borderRadius: "10px",
            boxShadow: "0 2px 6px rgba(0,0,0,0.1)",
          }}
        >
          <h3>Total Commits</h3>
          <h1>{data.total_commits}</h1>
        </div>

        <div
          style={{
            padding: "20px",
            background: "#ffffff",
            borderRadius: "10px",
            boxShadow: "0 2px 6px rgba(0,0,0,0.1)",
          }}
        >
          <h3>Pull Requests</h3>
          <h1>{data.pull_requests}</h1>
        </div>

        <div
          style={{
            padding: "20px",
            background: "#ffffff",
            borderRadius: "10px",
            boxShadow: "0 2px 6px rgba(0,0,0,0.1)",
          }}
        >
          <h3>Slack Messages</h3>
          <h1>{data.slack_messages}</h1>
        </div>

        <div
          style={{
            padding: "20px",
            background: "#ffffff",
            borderRadius: "10px",
            boxShadow: "0 2px 6px rgba(0,0,0,0.1)",
          }}
        >
          <h3>IDE Activity</h3>
          <h1>{data.ide_activity}</h1>
        </div>
      </div>

      <br />

      <h2>Status</h2>

      <p>🟢 Backend Connected Successfully</p>

      <p>
        <strong>Last Updated:</strong> {lastUpdated}
      </p>

      <hr />

      <footer>
        <p>CogniStream v1.0.0 | Week 1 Prototype</p>
      </footer>
    </div>
  );
}

export default App;