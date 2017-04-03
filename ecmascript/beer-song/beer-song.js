const verse = (beer) => {
	if ( beer == 0 ) {
		return `No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
`
	} else if ( beer == 1) {
		return `1 bottle of beer on the wall, 1 bottle of beer.
Take it down and pass it around, no more bottles of beer on the wall.
`
	} else if ( beer == 2) {
		return `${beer} bottles of beer on the wall, ${beer} bottles of beer.
Take one down and pass it around, ${beer-1} bottle of beer on the wall.
`
	} else {
		return `${beer} bottles of beer on the wall, ${beer} bottles of beer.
Take one down and pass it around, ${beer-1} bottles of beer on the wall.
`
	}
}

const sing = (...sing) => {
	const verses = [];
	let top, bottom ;

	if (sing.length == 2) {
		[top, bottom] = sing;
	} else if (sing.length == 1) {
		[top] = sing;
		bottom = 0;
	} else if (sing.length == 0) {
		top = 99;
		bottom = 0;
	}

	for (let i = top; i >= bottom; i--) {
		verses.push(verse(i));
	}
	return verses.join('\n')
}

export default { verse, sing }
