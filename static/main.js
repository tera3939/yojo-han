'use strict';

window.addEventListener('load', function () {
    const getSelectedRadio = (radios) => {
        for (const radio of radios) {
            if (radio.checked) {
                return radio.value;
            }
        }
        return null;
    };

    const buildActivity = (type, actor, object) => {
        return {
            '@context': 'https://www.w3.org/ns/activitystreams',
            'actor': actor,
            'object': object,
            'type': type
        };
    };

    const selectActivity = (action, actor, object_id) => {
        switch (action) {
            case 'follow':
                return buildActivity('Follow', actor, object_id);
            case 'unfollow':
                const follow_obj = buildActivity('Follow', actor, object_id);
                return buildActivity('Undo', actor, follow_obj);
            default:
                return null;
        }
    };

    const sendJson = (url, data) => {
        fetch(url,{
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/ld+json;charset=UTF-8'
            }
        }).then(res => {
            let result = document.getElementById('result');
            result.innerHTML = `<p>${res.status}: ${res.statusText}</p>`;
            result.innerHTML += "<p>";
            const render = res.body.getReader();
            const stream = new ReadableStream({
                start(controller) {
                    const push = () => {
                        render.read().then(({ done, value }) => {
                            if (done) {
                                controller.close();
                                return;
                            }

                            const chunk = new TextDecoder("utf-8").decode(value);
                            result.innerHTML += chunk;

                            controller.enqueue(value);
                            push();
                        });
                    };
                    push();
                }
            });
            result.innerHTML += "</p>";
            return new Response(stream, { headers: { "Content-Type": "text/html" } });
        })
        .catch(error => alert(error));
    };

    const validateUrl = (url, re) => {
        return re.test(url);
    };

    let send_button = document.getElementById('send_button');
    const url_regexp = /^https?:\/\/[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$/i;
    send_button.addEventListener('click', event => {
        const form = event.target.parentElement;
        const radios = form.querySelectorAll('input[name="action_radio"]');

        const action = getSelectedRadio(radios);
        const actor = form.querySelector('#actor_id').value;
        const object_id = form.querySelector('#object_id').value;
        if (!validateUrl(object_id, url_regexp)) {
            alert("invalid url");
            return null;
        }
        const url = new URL("/outbox", actor);

        sendJson(url, selectActivity(action, actor, object_id));
    });
});
