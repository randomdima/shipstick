// The demo's host (DEM-1): the page's socket replaced, before the page opens it, by a line that plays back the host's
// recording (DemoSite) on the page's own clock, in a loop — each frame sent when the host sent it, so the page animates
// as it does on a host. Nothing of the game runs here: an admin's `enter` switches to the recording of the capsule
// entered, and every other action is refused.
{
  const recording = fetch('demo/recording.json').then(answer => answer.json());
  const MS_PER_S = 1000;

  /** `value` with a FramePatch applied, `value` itself unchanged: `=` replaces, `o` patches keys, `a` elements. */
  function patched(value, patch) {
    if ('=' in patch) return patch['='];
    if ('o' in patch) {
      const next = { ...value };
      for (const [key, p] of Object.entries(patch.o)) next[key] = patched(value?.[key], p);
      for (const key of patch.d ?? []) delete next[key];
      return next;
    }
    const next = Array.from({ length: patch.n }, (_, i) => value?.[i] ?? null);
    for (const [i, p] of Object.entries(patch.a)) next[i] = patched(value?.[i], p);
    return next;
  }

  class RecordedLine {
    constructor(url) {
      const query = new URL(url).searchParams;
      recording.then(r => {
        this.recording = r;
        this.loopFromMs = performance.now();
        if (query.has('admin')) return this.play(Object.values(r.ship)[0]);
        const seat = query.get('seat');
        if (seat in r.seat) this.play(r.seat[seat]);
        else this.onclose?.({ reason: `seat refused: no capsule at seat ${seat}` });
      });
    }

    /** Plays `timeline` from where the loop stands now. */
    play(timeline) {
      Object.assign(this, { timeline, frame: null, next: 0 });
      this.tick();
    }

    /** Applies every change due by now, starting the loop again past its end, sends the frame, and waits for the next. */
    tick() {
      clearTimeout(this.timer);
      const { loopS } = this.recording;
      if ((performance.now() - this.loopFromMs) / MS_PER_S >= loopS) {
        this.loopFromMs += Math.floor((performance.now() - this.loopFromMs) / MS_PER_S / loopS) * loopS * MS_PER_S;
        Object.assign(this, { frame: null, next: 0 });
      }
      const nowS = (performance.now() - this.loopFromMs) / MS_PER_S;
      while (this.next < this.timeline.length && this.timeline[this.next][0] <= nowS)
        this.frame = patched(this.frame, this.timeline[this.next++][1]);
      this.show({ ...this.frame, nowS });
      const dueS = this.timeline[this.next]?.[0] ?? loopS;
      this.timer = setTimeout(() => this.tick(), (dueS - nowS) * MS_PER_S);
    }

    show(frame) {
      this.onmessage?.({ data: JSON.stringify(frame) });
    }

    send(text) {
      const { id, act, column, row } = JSON.parse(text);
      const entered = act === 'enter' ? this.recording?.ship[`${column},${row}`] : undefined;
      queueMicrotask(() => {
        this.onmessage?.({ data: JSON.stringify({ re: id, ok: entered !== undefined }) });
        if (entered) this.play(entered);
      });
    }
  }

  window.WebSocket = RecordedLine;
}
