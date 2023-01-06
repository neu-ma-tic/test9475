//https://stackoverflow.com/questions/5639346/what-is-the-shortest-function-for-reading-a-cookie-by-name-in-javascript
const getCookieValue = (name) => ( document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)')?.pop() || '' )

allBosses = ['110', '115', '120', '125', '130', '140', '155', '160', '165', '170', '180', '185', '190', '195', '200', '205', '210', '215', 'aggy', 'mord', 'hrung', 'necro', 'prot', 'gele', 'bt', 'dino']

function displayError(){
	document.getElementById('error').display = 'block'
}

function getTimerMinutes(timer){
	if (timer == null)
		return 'None'
	now = Math.round(Math.round(Date.now() / 1000) / 60)
	return timer - now
}

function logged(){
	user = document.getElementById('logged')
  api_key = getCookieValue('ApiKey')
  if(api_key != ''){
  	user.innerHTML = 'Logged'
  	document.getElementById('login').style.display = 'none'
		document.getElementById('timers').style.display = 'block'
		$.ajax({url: './api/get', type: 'POST', contentType: 'application/json', data: JSON.stringify({bosses: allBosses}), timeout: 10000, success: function(result){
			timers = result
			for (let boss of allBosses){
				document.getElementById(boss).innerHTML = getTimerMinutes(timers[boss])
			}
		}, error: function(xhr, status, error){
			displayError()
		}
	});
  }
}

function login(){
	$.ajax({url: './login', type: 'POST', data: {'ApiKey': document.getElementById('apikey').value}, timeout: 5000, success: function(result){
		logged()
	}, error: function(xhr, status, error){
			displayError()
	}})
}

function setTimer(boss_s, timer_s){
	$.ajax({url: './api/set', type: 'POST', contentType: 'application/json', data: JSON.stringify({boss: boss_s, timer: timer_s}), timeout: 5000, success: function(result){
		document.getElementById(boss_s).innerHTML = timer_s
	}, error: function(xhr, status, error){
			displayError()
	}})
}

function deleteTimer(boss_d){
	$.ajax({url: './api/set', type: 'POST', contentType: 'application/json', data: JSON.stringify({boss: boss_d, timer: 0}), timeout: 5000, success: function(result){
		document.getElementById(boss_d).innerHTML = 'None'
	}, error: function(xhr, status, error){
			displayError()
	}})
}