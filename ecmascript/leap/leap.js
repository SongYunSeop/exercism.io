
const isLeapYear = (year) => {
  const remainderIsZero = (x,y) => { return x % y === 0 }

  return remainderIsZero(year, 4) && (!remainderIsZero(year, 100) || remainderIsZero(year, 400))
  
}

export default isLeapYear;
