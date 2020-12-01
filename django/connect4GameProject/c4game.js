var fp = prompt("Enter first Player name");
var fpCol = 'rgb(86, 151 ,255)';

var sp = prompt("Enter second Player name")
var spCol = 'rgb(237, 45, 73)'

var game_ON = true;


var table = $('table tr')

function repotWin(rowNum,colNum)
{
    console.log("you won starting this row,column")
    console.log(rowNum)
    console.log(colNum)
}

function chColor(rowIdx,colIdx,color)
{
    //table--> tr --> td --> button
    return table.eq(rowIdx).find("td").eq(colIdx).find("button").css("background-color",color)
}


function ReportColor(rowIdx,colIdx)
{
    //table--> tr --> td --> button
    return table.eq(rowIdx).find("td").eq(colIdx).find("button").css('background-color')
}

function chckBottom(colIdx)
{
    var ColorReport = ReportColor(5,colIdx)
    for(var row=5;row>-1;row--)
    {
        console.log(row)
        ColorReport = ReportColor(row,colIdx)
        console.log(ColorReport)
        if(ColorReport==='rgb(202, 202, 202)')
        {
            return row
        }
    }
}


function colorMatch(one,two,three,four)
{
    return (one===two && one===three && one=== four && one!=='rgb(202, 202, 202)' && one !== undefined)
}


//horizontal win
function horizontalWinCheck(){
    for(var row = 0;row<6;row++)
    {
        for(var col =0;col<4;col++)
        {
            if(colorMatch(ReportColor(row,col),ReportColor(row,col+1),ReportColor(row,col+2),ReportColor(row,col+3)))
            {
                console.log("horiz")
                repotWin(row,col)
                return true;
            }
            else{
                continue;
            }

        }
    }
}


//vertical win
function verticalWinCheck(){
    for(var col = 0;col<7;col++)
    {
        for(var row =0;row<3;row++)
        {
            if(colorMatch(ReportColor(row,col),ReportColor(row+1,col),ReportColor(row+2,col),ReportColor(row+3,col)))
            {
                console.log("verti")
                repotWin(row,col)
                return true;
            }
            else{
                continue;
            }

        }
    }
}

//diagonal check
function diagCheck()
{
    for(var row = 0;row<6;row++)
    {
        for(var col =0;col<7;col++)
        {
            if(colorMatch(ReportColor(row,col),ReportColor(row+1,col+1),ReportColor(row+2,col+2),ReportColor(row+3,col+3)))
            {
                console.log("+ve diagonal")
                repotWin(row,col)
                return true;
            }
            else if(colorMatch(ReportColor(row,col),ReportColor(row+1,col-1),ReportColor(row+2,col-2),ReportColor(row+3,col-3)))
            {
                console.log("-ve diagonal")
                repotWin(row,col)
                return true;
            }
            else 
            {
                continue
            }

        }
    }
}

// Start Game

var currentPlayer = 1
var playerName = fp
var playerColor = fpCol

$('h2').eq(1).text(playerName+' it is your turn, pick up a column to drop in!')

$('.brd button').on('click',function ()
{
    var col = $(this).closest('td').index(); 
    console.log(col)
    var bottomAvailable = chckBottom(col)
    console.log(bottomAvailable)
    chColor(bottomAvailable,col,playerColor)
    if(horizontalWinCheck()||verticalWinCheck()||diagCheck())
    {
        $('h1').text(playerName+' You have won!!!')
        $('h2').fadeOut('fast')

    }
    currentPlayer = currentPlayer * -1

    if(currentPlayer===1)
    {
        playerName = fp
        playerColor = fpCol
    $('h2').eq(1).text(playerName+' it is your turn, pick up a column to drop in!')

    }
    else
    {
        playerName = sp
        playerColor = spCol
    $('h2').eq(1).text(playerName+' it is your turn, pick up a column to drop in!')
    }
    
}) 