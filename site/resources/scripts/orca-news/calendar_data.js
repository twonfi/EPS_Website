document.addEventListener('DOMContentLoaded', function() {
  let calendarEl = document.getElementById('calendar');
  let calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    headerToolbar: {
      left: 'prev,next today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
    },
    eventColor: '#623C5B',

    events: async function (fetchInfo, successCallback, failureCallback) {
        try {
          const response = await fetch(
            "/orca-news/data?api=a"
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
          alert("Events could not be loaded. Please try again later.");
          failureCallback(error);
        }},
  });
  calendar.render();

  document.getElementById('loading-message').remove();
  document.getElementById('body').setAttribute(
    'style', 'cursor: auto !important;');
});