/*
@everyone Make sure each file contains 
<div id="navbar"></div>
and this js file included
*/

document.getElementById("navbar").innerHTML = `
<nav>
    <ul class="navbar">
    <li><a href="/home">Home</a></li>
    <li><a href="/goals">Create Goal</a></li>
    <li><a href="/create-budget">Create Budget</a></li>
    <li><a href="/viewreport">Report</a></li>
    <li><a href="/transactions">Transactions</a></li>
    <li><a href="/register">Register</a></li>
    <li><a href="/login">Login</a></li>
    </ul>
</nav>
`;
