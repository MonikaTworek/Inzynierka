import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Router} from '@angular/router';

@Injectable({
  providedIn: 'root'
})

export class ConnectToBlackJackService {
  uid: number;

  constructor(private Client: HttpClient, private  router: Router) {
  }

  Register(number: number) {
    return this.Client.post('http://localhost:5000/register', {
      'numberof': number
    });
  }

  RememberID(uid: number) {
    this.uid = uid;
  }

  BeginGame() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/begin', {
      'bid': 10
    });
  }

  GenerateData(number: number) {
    return this.Client.post('http://localhost:5000/generate', {
      'numberof': number
    });
  }

  Hit1() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/action', {
      'action': 'hit1'
    });
  }

  Hit2() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/action', {
      'action': 'hit2'
    });
  }

  Stand1() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/action', {
      'action': 'stand1'
    });
  }

  Stand2() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/action', {
      'action': 'stand2'
    });
  }

  Double_down() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/action', {
      'action': 'double_down'
    });
  }

  Split() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/action', {
      'action': 'split'
    });
  }

  Insure() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/action', {
      'action': 'insure'
    });
  }

  Surrender() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/action', {
      'action': 'surrender'
    });
  }


  End_game() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/action', {
      'action': 'end_game'
    });
  }

  Finish_game() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/finish', {
      'numberof': 0
    });
  }
}
