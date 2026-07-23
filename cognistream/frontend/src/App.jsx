import "./App.css";
import {
  BarChart,
  Bar,
  PieChart,
  Pie,
  Cell,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
  RadialBarChart,
  RadialBar,
} from "recharts";

import { useEffect, useState } from "react";

function App() {
  const lastUpdated = new Date().toLocaleString();

  const [developer, setDeveloper] = useState("Salih");

  const [dashboard, setDashboard] = useState({
    developers: 0,
    commits: 0,
    pull_requests: 0,
    slack_messages: 0,
    ide_sessions: 0,
    total_events: 0,
  });

  const [data, setData] = useState({
    developer: "",
    events: 0,
    commits: 0,
    pull_requests: 0,
    slack_messages: 0,
    ide_activity: 0,
    total_minutes: 0,
    flow_score: 0,
  });

  useEffect(() => {
    fetch("http://127.0.0.1:8000/dashboard")
      .then((res) => res.json())
      .then((result) => setDashboard(result))
      .catch(console.log);
  }, []);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/developer/${developer}`)
      .then((res) => res.json())
      .then((result) => setData(result))
      .catch(console.log);
  }, [developer]);

  const flowState =
    data.total_minutes >= 350
      ? "🟢 High"
      : data.total_minutes >= 250
      ? "🟡 Medium"
      : "🔴 Low";

  const chartData = [
    { name: "Commits", value: data.commits },
    { name: "PRs", value: data.pull_requests },
    { name: "Slack", value: data.slack_messages },
    { name: "IDE", value: data.ide_activity },
  ];

  const flowGauge = [
    {
      name: "Flow Score",
      value: Math.min(data.flow_score, 100),
      fill: "#10B981",
    },
  ];

  const COLORS = ["#2563EB", "#10B981", "#F59E0B", "#EF4444"];

  

  return (
  <div className="app">
    
      
      <h1 className="title">🚀 CogniStream Dashboard</h1>
<p className="subtitle">
  Developer Flow-State & Cognitive Load Analytics
</p>



      {/* TEAM OVERVIEW */}

      <h2 className="section-title">📊 Team Overview</h2>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit,minmax(220px,1fr))",
          gap: "20px",
        }}
      >
        <div className="card">
          <h3>Developers</h3>
          <h1>{dashboard.developers}</h1>
        </div>

        <div className="card">
          <h3>Total Commits</h3>
          <h1>{dashboard.commits}</h1>
        </div>

        <div className="card">
          <h3>Pull Requests</h3>
          <h1>{dashboard.pull_requests}</h1>
        </div>

        <div className="card">
          <h3>Slack Messages</h3>
          <h1>{dashboard.slack_messages}</h1>
        </div>

        <div className="card">
          <h3>IDE Sessions</h3>
          <h1>{dashboard.ide_sessions}</h1>
        </div>

        <div className="card">
          <h3>Total Events</h3>
          <h1>{dashboard.total_events}</h1>
        </div>
      </div>

      <hr style={{ margin: "40px 0" }} />

      {/* Developer */}

      <h2 className="section-title">👨‍💻 Individual Analytics</h2>

      <select
  className="developer-select"
  value={developer}
  onChange={(e) => setDeveloper(e.target.value)}
>
        <option>Salih</option>
        <option>Anusha</option>
        <option>Meegadeesh</option>
      </select>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit,minmax(220px,1fr))",
          gap: "20px",
        }}
      >
        <div className="card">
          <h3>Commits</h3>
          <h1>{data.commits}</h1>
        </div>

        <div className="card">
          <h3>Pull Requests</h3>
          <h1>{data.pull_requests}</h1>
        </div>

        <div className="card">
          <h3>Slack Messages</h3>
          <h1>{data.slack_messages}</h1>
        </div>

        <div className="card">
          <h3>IDE Activity</h3>
          <h1>{data.ide_activity}</h1>
        </div>

        <div className="card">
          <h3>Total Coding Minutes</h3>
          <h1>{data.total_minutes}</h1>
        </div>

        <div className="card">
          <h3>Flow State</h3>
          <h1>{flowState}</h1>
        </div>
      </div>

      {/* Charts */}

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: "30px",
          marginTop: "40px",
        }}
      >
        <div className="chart-card">
          <h2>Developer Activity</h2>

          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={chartData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="value" fill="#2563EB" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="chart-card">
          <h2>Activity Distribution</h2>

          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={chartData}
                dataKey="value"
                outerRadius={100}
                label
              >
                {chartData.map((entry, index) => (
                  <Cell
                    key={index}
                    fill={COLORS[index]}
                  />
                ))}
              </Pie>

              <Legend />
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Flow Score */}

      <div className="chart-card">
        <h2>Flow Score Gauge</h2>

        <ResponsiveContainer width="100%" height={280}>
          <RadialBarChart
            innerRadius="70%"
            outerRadius="100%"
            data={flowGauge}
            startAngle={180}
            endAngle={0}
          >
            <RadialBar
              dataKey="value"
              cornerRadius={10}
            />
            <Legend />
          </RadialBarChart>
        </ResponsiveContainer>

        <h1 style={{ textAlign: "center" }}>
          {data.flow_score.toFixed(2)}
        </h1>
      </div>

      {/* Summary */}

      <div className="chart-card">
        <h2>Developer Summary</h2>

        <ul style={{ lineHeight: "2" }}>
          <li>Developer : {data.developer}</li>
          <li>Total Events : {data.events}</li>
          <li>Total Coding Minutes : {data.total_minutes}</li>
          <li>Commits : {data.commits}</li>
          <li>Pull Requests : {data.pull_requests}</li>
          <li>Slack Interruptions : {data.slack_messages}</li>
          <li>IDE Sessions : {data.ide_activity}</li>
          <li>Flow Score : {data.flow_score.toFixed(2)}</li>
          <li>
            Cognitive Load :
            {data.slack_messages > 2
              ? " High"
              : data.slack_messages === 2
              ? " Medium"
              : " Low"}
          </li>
        </ul>
      </div>

      {/* Status */}

      <div className="chart-card">
        <h2>Status</h2>

        <p>
          <strong>Backend:</strong> 🟢 Connected
        </p>

        <p>
          <strong>Flow State:</strong> {flowState}
        </p>

        <p>
          <strong>Last Updated:</strong> {lastUpdated}
        </p>
      </div>

      <footer className="footer">
        <hr />
        <p>CogniStream v1.0.0 | Week 2 Analytics Dashboard</p>
      </footer>
    </div>
  );
}

export default App;