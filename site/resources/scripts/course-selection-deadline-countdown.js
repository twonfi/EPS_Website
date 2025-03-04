window.addEventListener("load", async (event) => {
  try {
    console.log("Preparing to count down...");

    const response = await fetch('/resources/course-selection-deadline.txt');
    const deadlineString = await response.text();
    const deadline = new Date(deadlineString);
    console.log(`The deadline is ${deadlineString}`);
    console.log(deadline);

    const deadlineCountdown = document.getElementById('deadline-countdown');

    const updater = setInterval(function() {
      const now = new Date();
      const diff = deadline - now;
      if (diff <= 0) {
        deadlineCountdown.innerHTML = "Deadline passed";
        clearInterval(updater);
        console.log('Done; deadline passed!');
        return;
      }

      const days = Math.floor(diff / (1000 * 60 * 60 * 24));
      const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((diff % (1000 * 60)) / 1000);

      deadlineCountdown.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
    }, 1000);
  } catch (err) {
    console.error(err);
    // TODO: error handling stuff (e.g. "Deadline Unavailable")
  }
});
