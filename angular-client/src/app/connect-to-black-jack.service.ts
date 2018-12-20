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
    // return this.lastMessage;
    return {
      'bots_score': [
        {
          'Ekspansyjna': {
            'blackjack': 2,
            'draw': 0,
            'loosing': 5,
            'winning': 4
          }
        },
        {
          'ReagujNaBank': {
            'blackjack': 1,
            'draw': 1,
            'loosing': 4,
            'winning': 4
          }
        },
        {
          'HILow': {
            'blackjack': 1,
            'draw': 0,
            'loosing': 5,
            'winning': 5
          }
        },
        {
          'Intuicyjna': {
            'blackjack': 2,
            'draw': 0,
            'loosing': 5,
            'winning': 5
          }
        },
        {
          'Krupierska': {
            'blackjack': 1,
            'draw': 1,
            'loosing': 2,
            'winning': 6
          }
        },
        {
          'NeverBust': {
            'blackjack': 1,
            'draw': 0,
            'loosing': 6,
            'winning': 4
          }
        },
        {
          'Prawdopodobna': {
            'blackjack': 1,
            'draw': 0,
            'loosing': 0,
            'winning': 1
          }
        },
        {
          'PrzelamPasse': {
            'blackjack': 2,
            'draw': 1,
            'loosing': 4,
            'winning': 5
          }
        },
        {
          'PrzetrzymajPasse': {
            'blackjack': 1,
            'draw': 1,
            'loosing': 2,
            'winning': 6
          }
        },
        {
          'Podstawowa': {
            'blackjack': 2,
            'draw': 1,
            'loosing': 2,
            'winning': 7
          }
        },
        {
          'ZaleznaOdSzczescia': {
            'blackjack': 2,
            'draw': 1,
            'loosing': 4,
            'winning': 5
          }
        },
        {
          'Pasujaca': {
            'blackjack': 1,
            'draw': 0,
            'loosing': 7,
            'winning': 4
          }
        },
        {
          'Idealna': {
            'blackjack': 2,
            'draw': 1,
            'loosing': 1,
            'winning': 8
          }
        }
      ],
      'header': 'success',
      'player_score': {
        'blackjack': 1,
        'draw': 0,
        'loosing': 0,
        'winning': 1
      }
    };
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
