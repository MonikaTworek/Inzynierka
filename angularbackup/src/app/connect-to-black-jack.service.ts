import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Router} from '@angular/router';
import {catchError, map} from 'rxjs/internal/operators';
import {of} from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class ConnectToBlackJackService {
  uid: number;
  lastMessage: any;
  first_blackjack: boolean;
  whoWin: string;

  constructor(private Client: HttpClient, private  router: Router) {
  }

  SetFirst (set: boolean, win: string) {
    this.first_blackjack = set;
    this.whoWin = win;
  }

  GetFirst() {
    return this.first_blackjack;
  }

  GetWin() {
    return this.whoWin;
  }

  Update(tekst: any) {
    this.lastMessage = tekst;
  }

  Set() {
    return this.lastMessage;
  }

  Register(number: number) {
    return this.Client.post('http://localhost:5000/register', {
      'numberof': number
    });
  }

  RememberID(uid: number) {
    this.uid = uid;
  }

  handleEndGameError(res) {
    if (res.error && res.error.message && res.error.message === 'You finish') {
      return of({'end_game': true});
    }
    return of(res);
  }

  BeginGame() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/begin', {
      'bid': 10
    }).pipe(catchError(this.handleEndGameError));
  }

  GenerateData(number: number) {
    return this.Client.post('http://localhost:5000/generate', {
      'numberof': number
    });
  }

  Hit1() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/action', {
      'action': 'hit1'
    }).pipe(catchError(this.handleEndGameError));
  }

  Hit2() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/action', {
      'action': 'hit2'
    }).pipe(catchError(this.handleEndGameError));
  }

  Stand1() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/action', {
      'action': 'stand1'
    }).pipe(catchError(this.handleEndGameError));
  }

  Stand2() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/action', {
      'action': 'stand2'
    }).pipe(catchError(this.handleEndGameError));
  }

  Double_down() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/action', {
      'action': 'double_down'
    }).pipe(catchError(this.handleEndGameError));
  }

  Split() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/action', {
      'action': 'split'
    }).pipe(catchError(this.handleEndGameError));
  }

  Insure() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/action', {
      'action': 'insure'
    });
  }

  Surrender() {
    return this.Client.post('http://localhost:5000/player/' + this.uid + '/action', {
      'action': 'surrender'
    }).pipe(catchError(this.handleEndGameError));
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
