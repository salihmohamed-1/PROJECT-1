function App() {
  return (
    <div
      style={{
        padding: "40px",
        fontFamily: "Arial, sans-serif",
        backgroundColor: "#f5f5f5",
        minHeight: "100vh",
      }}
    >
      <h1>🚀 CogniStream Dashboard</h1>

      <p>Developer Productivity Analytics</p>

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
            background: "white",
            borderRadius: "10px",
          }}
        >
          <h3>Total Commits</h3>
          <h1>0</h1>
        </div>

        <div
          style={{
            padding: "20px",
            background: "white",
            borderRadius: "10px",
          }}
        >
          <h3>Pull Requests</h3>
          <h1>0</h1>
        </div>

        <div
          style={{
            padding: "20px",
            background: "white",
            borderRadius: "10px",
          }}
        >
          <h3>Slack Messages</h3>
          <h1>0</h1>
        </div>

        <div
          style={{
            padding: "20px",
            background: "white",
            borderRadius: "10px",
          }}
        >
          <h3>IDE Activity</h3>
          <h1>0</h1>
        </div>
      </div>

      <br />

      <h2>Status</h2>

      <p>🟡 Backend connection will be added in Week 2.</p>
    </div>
  );
}

export default App;