
class Gigasecond {
  constructor(datetime) {
    this.datetime = datetime;
  }

  date() {
    // gigasecond == 10^9 s == 10^12 ms
    return new Date(this.datetime.getTime() + (10**12))
  }
}

export default Gigasecond;
