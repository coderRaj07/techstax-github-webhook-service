async function loadEvents() {
  const res = await fetch("/events");
  const data = await res.json();

  const container = document.getElementById("events");
  container.innerHTML = "";

  data.forEach(e => {
    let text = "";

    if (e.action === "PUSH") {
      text = `${e.author} pushed to ${e.to_branch} on ${e.timestamp}`;
    } else if (e.action === "PULL_REQUEST") {
      text = `${e.author} submitted a pull request from ${e.from_branch} to ${e.to_branch} on ${e.timestamp}`;
    } else if (e.action === "MERGE") {
      text = `${e.author} merged branch ${e.from_branch} to ${e.to_branch} on ${e.timestamp}`;
    }

    const div = document.createElement("div");
    div.className = "event";
    div.innerText = text;
    container.appendChild(div);
  });
}

loadEvents();
setInterval(loadEvents, 15000);
