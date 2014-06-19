(function () {
	"use strict";

	var FORMDATA_SUPPORT = 'FormData' in window,
		$popupTab = $(".zf-popup-tab"),
		$popup = $("#ZenaidaFeedback"),
		$form = $("#ZenaidaFeedback form"),
		$popupBody = $(".zf-body"),
		$submitButton = $("#ZenaidaFeedback form button"),
		$messageContainer = $(".zf-message-container"),
		initial_submit_text = $submitButton.text(),
		bind_submit = function () {
			$form.one("submit", on_submit);
		},
		on_submit = function (e) {
			// If HTML5 FormData support exists, file-uploads will work.
			// Otherwise jQuery.fn.serialize ignores file inputs.
			var form_data = FORMDATA_SUPPORT ? new FormData($form[0]) : $form.serialize();

			// Adjust the submit button:
			$submitButton.attr("disabled", "disabled");
			$submitButton.css({"opacity":.5});
			$submitButton.text("Submitting...");

			// Clear the message container:
			$messageContainer.html("");

			$.ajax({
				type: $form.attr('method'),
				url: $form.attr('action'),
				data: form_data,
				dataType: 'json',
				// Let jQuery process the data only if FormData is not supported:
				processData: !FORMDATA_SUPPORT,
				// Content type also depends on FormData support:
				contentType: FORMDATA_SUPPORT ? false : 'application/x-www-form-urlencoded; charset=UTF-8',
				success: function (data) {
					$popupBody.html("<div class='zf-thanks'>" + data.message + "</div>");
				},
				error: function (jqx, status, err) {
					var error_data;
					if (err == "BAD REQUEST") {
						// If it's a 400 error, process the returned response:
						error_data = $.parseJSON(jqx.responseText);
						$.each(error_data, function (k, v) {
							// Add error to the message container:
							var message;
							if (v[0].code == "required") {
								message = "Field <b>" + k + "</b> is required.";
							} else {
								message = '<b>'+ k +':</b> ' + v[0].message
							}
							$messageContainer.append('<div class="zf-message-error">' + message + '</div>');
						});
					} else {
						// If it's not a 400 error, I have no idea what's going on.
						$messageContainer.append('<div class="zf-message-error">An unknown error occurred: ' + err + '. Please email a site administrator directly.</div>');
					}
					// Readjust button for resubmission:
					$submitButton.removeAttr("disabled");
					$submitButton.css({"opacity": 1});
					$submitButton.text(initial_submit_text);
					// Rebind the submit event:
					bind_submit();
				}
			});
		};

	// toggle the feedback form when clicking on the tab
	$popupTab.click(function () {
		$popup.toggleClass("in");
	});

	if (!FORMDATA_SUPPORT) {
		// Asynchronous file upload not supported:
		$('#zf-screenshot-group').hide();
	}

	$form.on("submit", function (e) { e.preventDefault(); }); // always prevent the form from submitting
	bind_submit(); // allow the form to make an ajax call only once

}());
