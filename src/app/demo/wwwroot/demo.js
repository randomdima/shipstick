// The demo's host (DEM-1): the page's socket replaced, before the page opens it, by a line that plays back the host's
// recorded frames (DemoSite). Nothing of the game runs here: an admin's `enter` is answered with the recording of the
// capsule entered, and every other action is refused.
{
  const recording = fetch('demo/frames.json').then(answer => answer.json());

  class RecordedLine {
    constructor(url) {
      const query = new URL(url).searchParams;
      recording.then(frames => {
        this.frames = frames;
        if (query.has('admin')) return this.show(Object.values(frames.ship)[0]);
        const seat = query.get('seat');
        if (seat in frames.seat) this.show(frames.seat[seat]);
        else this.onclose?.({ reason: `seat refused: no capsule at seat ${seat}` });
      });
    }

    show(frame) {
      this.onmessage?.({ data: JSON.stringify(frame) });
    }

    send(text) {
      const { id, act, column, row } = JSON.parse(text);
      const entered = act === 'enter' ? this.frames?.ship[`${column},${row}`] : undefined;
      queueMicrotask(() => {
        this.onmessage?.({ data: JSON.stringify({ re: id, ok: entered !== undefined }) });
        if (entered) this.show(entered);
      });
    }
  }

  window.WebSocket = RecordedLine;
}
