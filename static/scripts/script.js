$(document).ready(function () {
  /**
   * Checks if there is any input within the fields of the forms
   * If any mandatory field is empty, disables access to the submit button.
   */
  $("#urlForm").on("focusout keydown keyup", function () {
    urlToShorten = $("#urlNameID").val();
    if (urlToShorten == "" || !urlToShorten.includes(".")) {
      // if input field is empty, disables the submission button and display error to user.
      $("#urlNameID").addClass("is-danger");
      $("#urlInputWarn").html("Please enter a valid URL such as: 'http://google.com' or 'payroc.com'.");
      $("#generateLinkButton").prop("disabled", true);
    } else {
      // If the field has valid input, enables button and removes error message.
      $("#urlNameID").removeClass("is-danger");
      $("#urlInputWarn").html("");
      $("#urlNameID").addClass("is-success");
      $("#generateLinkButton").prop("disabled", false);
    }
  });
});
