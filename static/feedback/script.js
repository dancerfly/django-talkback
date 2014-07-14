(function () {
	"use strict";

	var $,
		zf_feedback = window.zf_feedback = {};

	// Keep track of divs that need to be cleaned up sometimes:
	zf_feedback.message_divs = [];

	if ('jQuery' in window && typeof jQuery !== "undefined") {
		$ = jQuery;
	} else if ('zf' in window && 'jQuery' in window.zf) {
		$ = zf.jQuery;
	} else {
		if ('console' in window) console.warn("Zenaida feedback does not work without jQuery. Please specify FEEDBACK_CONFIG['JQUERY_URL'] in settings.py.");
		// Without jQuery, there's no sense in displaying the form:
		var el = document.getElementById('ZenaidaFeedback');
		el.parentNode.removeChild(el);
		return;
	}

	var FORMDATA_SUPPORT = 'FormData' in window,
		$popupTab = $(".zf-popup-tab"),
		$popup = $("#ZenaidaFeedback"),
		$form = $("#ZenaidaFeedback form"),
		$popupBody = $(".zf-body"),
		$submitButton = $("#ZenaidaFeedback form button"),
		$errorMessage = $(".zf-message-error"),
		$thanksMessage = $(".zf-message-thanks"),
		initial_submit_text = $submitButton.text(),
		bind_submit = function () {
			$form.one("submit", on_submit);
		},
		create_error_message = function (message_content) {
			// Create the message div:
			var message = $errorMessage.clone().html(message_content).show();
			// Keep track of this div:
			zf_feedback.message_divs.push(message);
			// Append after the error message template:
			$errorMessage.after(message);
		},
		clear_error_messages = function () {
			// Clear the message divs:
			for (var i = 0; i < zf_feedback.message_divs.length; i++) {
				zf_feedback.message_divs[i].remove();
				zf_feedback.message_divs.splice(0, 1);
			}
		},
		on_submit = function (e) {
			// If HTML5 FormData support exists, file-uploads will work.
			// Otherwise jQuery.fn.serialize ignores file inputs.
			var form_data = FORMDATA_SUPPORT ? new FormData($form[0]) : $form.serialize();

			// Adjust the submit button:
			$submitButton.attr("disabled", "disabled");
			$submitButton.css({"opacity":.5});
			$submitButton.text(zf_feedback.l10n.submitting);

			clear_error_messages();

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
					$form.hide();
					$thanksMessage.html(data.message);
					$thanksMessage.show();
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
								message = zf_feedback.l10n.required_field.replace("__FIELDNAME__", "<b>" + k + "</b>");
							} else {
								message = '<b>'+ k +':</b> ' + v[0].message
							}
							create_error_message(message);
						});
					} else {
						// If it's not a 400 error, I have no idea what's going on.
						create_error_message(zf_feedback.l10n.unknown_error.replace("__ERR__", err))
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

	// Hide the message templates/divs:
	$('.zf-message').hide()

	if (!FORMDATA_SUPPORT) {
		// Asynchronous file upload not supported:
		$('#zf-screenshot-group').hide();
	}

	$form.on("submit", function (e) { e.preventDefault(); }); // always prevent the form from submitting
	bind_submit(); // allow the form to make an ajax call only once

}());
