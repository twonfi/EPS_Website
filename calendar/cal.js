window.addEventListener("load", function () {
    var calendarEl = document.getElementById("calendar");
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: "dayGridMonth",
        headerToolbar: {left: "prev,next today",
            center: "title",
            right: "dayGridMonth,timeGridWeek,timeGridDay",
          },
          events: async function (fetchInfo, successCallback, failureCallback) {
            try {
              const response = await fetch(
                  // DO NOT USE IN PRODUCTION I'LL THINK OF BETTER WAY
                  // (but it would probably be used anyways)

                  // we can use /orca_news/cal if Appazur blocks the proxy's IP or if the proxy blocks us
                "https://api.codetabs.com/v1/proxy?quest=elginpark.appazur.com/api/a?age=30&ua=1&v=2"
              );
              const data = await response.json();

              const events = data.map((event) => {
                return {
                  title: event.name,
                  start:
                    event.date + (event.start24 ? "T" + event.start24 : ""),
                  end: event.end ? event.date + "T" + event.end : null,
                };
              });

              successCallback(events);
            } catch (error) {
              console.error("Error fetching events:", error);
              failureCallback(error);
            }},
    });
    calendar.render();
});