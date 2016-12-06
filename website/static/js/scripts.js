/* No longer using jQuery
 * $('a[href="' + this.location.pathname + '"]').parents('li,ul').addClass('active');
 */
var list = document.getElementById("navigation").querySelectorAll("a");
for(let link of list) {
    if(link.pathname === this.location.pathname) {
        link.classList.add("active");
    } else {
        link.classList.add("transition");
    }
}
/* var list = document.querySelectorAll("a[href='" + this.location.pathname + "']");
 * for(let link of list) {
 *     if(link.parentElement.nodeName == "LI")
 *         //link.parentElement.classList.add("active");
 *         link.classList.add("active");
 * }
 */
