document.addEventListener('DOMContentLoaded', function() {
  let calendarEl = document.getElementById('calendar');
  let calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    headerToolbar: {
      left: 'prev,next today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
    },
    navLinks: true,
    eventColor: '#623C5B',
    validRange: {
      // only show 30 days back and 12 months forward
      start: new Date(new Date().setDate(new Date().getDate() - 30)),
      end: new Date(new Date().setDate(new Date().getDate() + 365))
    },
    nowIndicator: true,
    // businessHours: {
    //   daysOfWeek: [1, 2, 3, 4, 5],
    //   startTime: '08:30',
    //   endTime: '16:43'
    // },

    events: async function (fetchInfo, successCallback, failureCallback) {
        try {
          const response = await fetch(
            "/orca-news/data?api=a"
          );
          const data = await response.json();

          const events = data.map((event) => {
            return {
              title: event.name,
              start: event.date + (event.start24 ? "T" + event.start24 : ""),
              end: event.end ? event.date + "T" + event.end : null,
            };
          });

          successCallback(events);
        } catch (error) {
          console.error("Error fetching events:", error);
          alert("Events could not be loaded. Please try again later.");
          failureCallback(error);
        }},
    eventClassNames: function(arg) {
      if (arg.event['title'] === "A-B-C-D" ||
          arg.event['title'] === "B-A-D-C" ||
          arg.event['title'] === "C-D-A-B" ||
          arg.event['title'] === "D-C-B-A") {
        return [ 'block-order' ]
      }
    }
  });
  calendar.render();

  document.getElementById('loading-message').remove();
  document.getElementById('body').setAttribute(
    'style', 'cursor: auto !important;');
});